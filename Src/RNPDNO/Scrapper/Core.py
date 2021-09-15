from typing import Union

from pymongo.common import _AUTH_OPTIONS
from RNPDNO.Config import ConfigReader

import logging

logger = logging.getLogger(__name__)

class Scrapper:

    class Exceptions:

        class ConfigNotLoaded(Exception):
            pass

        class SessionNotCreated(Exception):
            pass

        class TemplateNotFound(Exception):
            pass

        class MultipleTemplatesFound(Exception):
            pass

        class InvalidTemplate(Exception):
            pass

    def __init__(self) -> None:
        
        self.__config_loaded = False
    @staticmethod
    def validate_request_template(template: dict) -> bool:

        list_of_expected_keys = ["api", "endpoint", "url", "host", "method", "payloadTemplate"]
        list_of_actual_keys =template.keys()

        list_of_missing_keys = [key for key in list_of_expected_keys if key not in list_of_actual_keys]

        if len(list_of_missing_keys) > 0:
            return False
        else:
            return True

    def check_config_loaded(self, error: bool = True) -> bool:
        """Check if app configuration has been loaded

        Args:
            error (bool, optional): Should an exception be raised if the configuration is not loaded? Defaults to True.

        Raises:
            ConfigNotLoaded: If configuration is not loaded and error is set to True.

        Returns:
            bool: Configuration is loaded?
        """

        if self.__config_loaded:
            return True
        elif error:
            raise self.Exceptions.ConfigNotLoaded("Configuration must be loaded first via the load_config method!")
        else:
            return False

    def check_session_created(self, error: bool = True) -> bool:
        """Check if instance requests session has been created

        Args:
            error (bool, optional): Should an exception be raised if the requests session has not been created?. Defaults to True.

        Raises:
            self.Exceptions.SessionNotCreated: If the requests session is not created and error is set to True.

        Returns:
            bool: Requests session has been created?
        """

        if self.__session_created:
            return True
        elif error:
            raise self.Exceptions.SessionNotCreated("The request session must be created first via the create_session method!")
        else:
            return False

    @property
    def config(self) -> ConfigReader:
        """App config

        Get the application configuration object.

        Returns:
            ConfigReader: An object of class ConfigReader containing the current application configuration.
        """
        return self.__config_reader

    @property
    def env_vars(self) -> dict:
        """Environment variables

        Returns:
            dict: A dict containing the environment variables detected by the application's ConfigReader.
        """
        return self.config.app_vars

    @property
    def request_templates(self) -> list:

        self.check_config_loaded()

        return self.__request_templates

    @property
    def session(self) -> requests.Session:
        """Scrapper requests session

        Returns:
            requests.Session: Scrapper requests session.
        """

        self.check_session_created()

        return self.__session

    @property
    def TARGETDB_NAME(self) -> str:
        """Target MongoDB name

        The target MongoDB is the DB where the scrapped information is to be stored.

        Raises:
            ValueError: If app configuration is not loaded before calling this property.

        Returns:
            str: Target MongoDB name.
        """

        self.check_config_loaded()

        return self.__target_db_name

    @property
    def TARGETDB_USERNAME(self) -> str:
        """Target MongoDB username

        Raises:
            ValueError: If app configuration is not loaded before calling this property.

        Returns:
            str: Target MongoDB username.
        """

        self.check_config_loaded()

        return self.__target_db_username

    @property
    def TARGETDB_PASSWORD(self) -> str:
        """Target MongoDB password

        Raises:
            ValueError: If app configuration is not loaded before calling this property.

        Returns:
            str: Target MongoDB password.
        """

        self.check_config_loaded()

        return self.__target_db_password

    def create_requests_session(self) -> None:

        logger.info("Creating new requests session...")
        self.__session = requests.Session()
        self.__session_created = True
        logger.info("Session created!")

    def set_common_config_variables(self) -> None:
        """Set common configuration variables as class properties

        Raises:
            ValueError: If app configuration is not loaded before calling this method.
        """

        self.check_config_loaded()

        self.__target_db_name = self.config["SCRAPPER_MONGO_TARGETDB_NAME"]
        self.__target_db_username = self.config["SCRAPPER_MONGO_TARGETDB_USERNAME"]
        self.__target_db_password = self.config["SCRAPPER_MONGO_TARGETDB_PASSWORD"]

    def load_config(self) -> None:
        """Load app configuration
        """

        logger.info("Initializing new instance of configuration reader object...")
        self.__config_reader = ConfigReader()

        logger.info("Starting configuration loading routine...")
        # Load environment variables
        self.config.load_env_vars()
        # Load configuration from db
        self.config.load_config(collection = "config_vars")

        # Load request templates from DB
        self.__request_templates = self.config.load_config(collection = "request_templates")

        self.__config_loaded = True

        logger.info("App configuration loaded!")

    def get_request_template(self, api_name: str, end_point: str, error: bool = False) -> Union[dict, None]:
        
        logger.info("Looking for request template (api: %s, end_point: %s)...", api_name, end_point)
        search_result = next( (doc for doc in self.request_templates if doc["api"] == api_name and doc["endPoint"] == end_point), None )

        if search_result is None:
            msg = "The request template doesn't exist! (api: {0}, end_point: {1})".format(api_name, end_point)
            if error:
                raise self.Exceptions.TemplateNotFound(msg)
            else:
                logger.warning(msg)
                return None

        if len(search_result) > 1:
            msg = "The search query returned more than one template (api: {0}, end_point: {1})".format(api_name, end_point)
            if error:
                raise self.Exceptions.MultipleTemplatesFound(msg)
            else:
                logger.warning(msg)
                return None

        return search_result

    def get_totals(self, state_ida: str = "0", mun_id: str = "0", neighborhood_id: str = "0", date_start: str = "", date_ent: str = "", **kwargs) -> dict:
        pass

    def get_missing_by_neighborhood(self, state_id: str, mun_id: str, neighborhood_id: str = "0", **kwargs) -> dict:
        pass
