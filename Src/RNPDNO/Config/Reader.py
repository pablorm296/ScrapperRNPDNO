import pymongo as pm
from pymongo.errors import ConnectionFailure

from typing import Union

import logging
import re
import os

# Init logger
logger = logging.getLogger(__name__)

class ConfigReader(dict):

    def __init__(self):

        # Call parent class' init method
        super().__init__()

        self.__app_vars = None
        self.__config_db_conn = None
        self.__app_vars_loaded = False

    @property
    def config_db_conn(self) -> pm.MongoClient:
        return self.__config_db_conn

    @property
    def app_vars(self) -> dict:
        return self.__app_vars

    def test_config_db_conn(self) -> bool:

        if self.config_db_conn is None:
            logger.warning("The Mongo client has not been initialized!")
            return False

        try:
            # The ismaster command is cheap and does not require auth.
            self.config_db_conn.admin.command("ismaster")
        except ConnectionFailure:
            logger.error("Failed to connect to the Mongo server!")
            return False
        else:
            return True

    def open_new_config_db_conn(self) -> None:

        # Define the mongo uri
        mongo_uri = "mongodb://{username}:{password}@{host}:{port}/{db}".format(
            username = self.app_vars["SCRAPPER_MONGO_CONFIGDB_USERNAME"],
            password = self.app_vars["SCRAPPER_MONGO_CONFIGDB_PASSWORD"],
            host = self.app_vars["SCRAPPER_MONGO_HOST"],
            port = self.app_vars["SCRAPPER_MONGO_PORT"],
            db = self.app_vars["SCRAPPER_MONGO_CONFIGDB_NAME"]
        )

        # Open a new connection to the database
        logger.info("Opening new connection to the config DB...")
        logger.debug("Mongo URI used to connect to the new config DB: %s", mongo_uri)
        self.__config_db_conn = pm.MongoClient(mongo_uri)

    def load_env_vars(self) -> None:
        """Set environment configuration variables

        Environment configuration variables are stored in the `app.vars` attribute.

        This is the list of available configuration variables:
        * SCRAPPER_MONGO_HOST: Mongo DB host name.
        * SCRAPPER_MONGO_PORT: Mongo DB port number.
        * SCRAPPER_MONGO_CONFIGDB_USERNAME: Mongo DB user name.
        * SCRAPPER_MONGO_CONFIGDB_PASSWORD: Mongo DB password.
        * SCRAPPER_MONGO_CONFIGDB_NAME: Name of the Mongo DB name with the app config. 

        Returns:
            None
        """
        
        # Get all the env vars
        logger.info("Loading environment variables...")
        env_vars = os.environ

        # Coerce as dict
        env_vars = dict(env_vars)

        # Init app vars container
        self.__app_vars = {}

        # Loop through each environment variable
        # We must keep in app_vars all env variables with the prexix SCRAPPER_
        for var in env_vars:
            # Test var name
            is_scrapper_var = True if re.match(r"SCRAPPER_", var) is not None else False

            if is_scrapper_var:
                self.__app_vars[var] = env_vars[var]

        logger.info("%s environment variables were loaded.", len(self.__app_vars))
        logger.debug("The following environment variables were loaded: %s", self.__app_vars)

        self.__app_vars_loaded = True

    def load_config(self, collection = "config_vars") -> Union[None, dict]:

        logger.info("Loading app configuration from DB (target collection: %s)...", collection)

        # Check if env vars have been loaded
        if not self.__app_vars_loaded:
            raise ValueError("Environment variables must be loaded before loading the app configuration!")

        # Open new connection
        self.open_new_config_db_conn()
        
        if not self.test_config_db_conn():
            raise ConnectionError("Can't load the app config, since there's not a valid connection to a Mongo host!")

        # Get app_config db
        app_config_db = self.config_db_conn[self.app_vars["SCRAPPER_MONGO_CONFIGDB_NAME"]]

        logger.info("Successful connection to the config DB!")

        # Get app_config_vars collection
        app_config_vars_collection = app_config_db[collection]

        if collection == "config_vars":
            logger.debug("Registering configuration variables to self, since collection is config_vars...")

            # Loop through each doc and register to self
            for document in app_config_vars_collection.find():
                # Get config variable name
                var_name = document["name"]
                # Get config variable value
                var_value = document["value"]

                # Register to self
                self.update({var_name: var_value})

            logger.info("%s configuration variables were loaded!", len(self))
        else:
            return_dict = {}

            # Loop through each doc and register to return_dict
            for document in app_config_vars_collection.find():
                # Get config variable name
                var_name = document["name"]
                # Get config variable value
                var_value = document["value"]

                # Register to self
                return_dict.update({var_name: var_value})

            logger.info("%s configuration variables were loaded!", len(return_dict))

            return return_dict
