from typing import Union, cast

from RNPDNO.Config import ConfigReader

import requests

import logging

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
        self.__session_created = False

        self.__session = None
        self.__config_reader = None

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

    def create_logger(self, level: int, name:str = "Scrapper.logger", format:str = "%(asctime)s | %(levelname)7s @ %(filename)s : %(message)s", date_format = "%Y-%m-%d %H:%M:%S"):

        logging.info("Creating new logger instance at Scrapper instance...")

        # Create logger
        self.__logger = logging.getLogger(name)

        # Create a console handler
        self.__logger_stream_handler = logging.StreamHandler()
        # Set level
        self.__logger_stream_handler.setLevel(level)

        # Create a log formatter
        self.__logger_stream_formatter = logging.Formatter(fmt = format, datefmt = date_format)
        
        # Assign stream formatter to stream handler
        self.__logger_stream_handler.setFormatter(self.__logger_stream_formatter)

        self.logger.info("Logger instance created!")

    @property
    def logger(self):

        return self.__logger

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
        """Request templates

        Returns:
            list: A list of request templates (dicts).
        """

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

        self.logger.info("Creating new requests session...")
        self.__session = requests.Session()
        self.__session_created = True
        self.logger.info("Session created!")

    def send_request(self, method:str, url:str, **kwargs) -> requests.Response:

        self.logger.info("Sending {0} request to {1}...".format(method, url))
        
        self.check_session_created()

        r = self.session.request(method = method, url = url, **kwargs)

        return r

    def send_request_from_template(self, template: dict, payload: dict = None) -> requests.Response:
        
        if not self.validate_request_template(template):
            msg = "The supplied template is not valid!"
            self.logger.error(msg)
            raise self.Exceptions.InvalidTemplate(msg)

        # Get request args
        request_method = template["method"]
        request_url = "{0}{1}".format(template["host"], template["url"])
        request_payload = template["payload"]

        # Check if payload is None
        if request_payload is not None:
            self.logger.debug("Payload object is not None, therefore contents will update the payload template.")
            self.logger.debug("Request template: {0}".format(request_payload))
            self.logger.debug("User suplied payload: {0}".format(payload))

            request_payload = {**request_payload, **payload}

            self.logger.debug("Updated payload: {0}".format(request_payload))

        r = self.send_request(method = request_method, url = request_url, data = request_payload)

        return r

    def initialize_requests_sessions(self) -> None:
        
        self.logger.info("Initializing requests session...")
        self.check_session_created()

        template_index = self.get_request_template(api_name = "dashboard", end_point = "index")
        template_home = self.get_request_template(api_name = "dashboard", end_point = "home")

    def set_common_config_variables(self) -> None:
        """Set common configuration variables as class instance properties

        Raises:
            ValueError: If app configuration is not loaded before calling this method.
        """
        
        self.logger.info("Setting common config variables as class instance properties...")
        self.check_config_loaded()

        self.__target_db_name = self.config["SCRAPPER_MONGO_TARGETDB_NAME"]
        self.__target_db_username = self.config["SCRAPPER_MONGO_TARGETDB_USERNAME"]
        self.__target_db_password = self.config["SCRAPPER_MONGO_TARGETDB_PASSWORD"]

    def load_config(self) -> None:
        """Load app configuration
        """

        self.logger.info("Initializing new instance of configuration reader object...")
        self.__config_reader = ConfigReader()

        self.logger.info("Starting configuration loading routine...")
        # Load environment variables
        self.config.load_env_vars()
        # Load configuration from db
        self.config.load_config(collection = "config_vars")

        # Load request templates from DB
        self.__request_templates = self.config.load_config(collection = "request_templates")

        self.__config_loaded = True

        self.logger.info("App configuration loaded!")

    def get_request_template(self, api_name: str, end_point: str, error: bool = False) -> Union[dict, None]:
        """Get a specific request template by API name and end-point name.

        Args:
            api_name (str): Name of the API.
            end_point (str): Name of the end-point.
            error (bool, optional): Should an exception be raised if the query returns more than one template or no template at all?. Defaults to False.

        Raises:
            self.Exceptions.TemplateNotFound: Exception raised when no templates match the search query.
            self.Exceptions.MultipleTemplatesFound: Exception raised when multiple templates match the search query.

        Returns:
            dict: Request template.
            None: If no templates or multiple templates are found.
        """
        
        self.logger.info("Looking for request template (api: %s, end_point: %s)...", api_name, end_point)
        search_result = next( (doc for doc in self.request_templates if doc["api"] == api_name and doc["endPoint"] == end_point), None )

        if search_result is None:
            msg = "The request template doesn't exist! (api: {0}, end_point: {1})".format(api_name, end_point)
            if error:
                raise self.Exceptions.TemplateNotFound(msg)
            else:
                self.logger.warning(msg)
                return None

        if len(search_result) > 1:
            msg = "The search query returned more than one template (api: {0}, end_point: {1})".format(api_name, end_point)
            if error:
                raise self.Exceptions.MultipleTemplatesFound(msg)
            else:
                self.logger.warning(msg)
                return None

        return search_result

    def get_states_catalogue(self):
        pass

    def get_municipalities_catalogue(self, state_id: str):
        pass

    def get_neighborhood_catalogue(self, state_id: str, mun_id: str):
        pass

    def get_totals(self, state_id: str = "0", mun_id: str = "0", neighborhood_id: str = "0", date_start: str = "", date_ent: str = "", **kwargs) -> dict:
        pass

    def get_missing_by_neighborhood(self, state_id: str, mun_id: str, neighborhood_id: str = "0", **kwargs) -> dict:
        pass
