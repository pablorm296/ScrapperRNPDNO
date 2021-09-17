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

        class UnsuccessfulRequest(Exception):
            pass

    def __init__(self) -> None:
        
        self.__config_loaded = False
        self.__session_created = False

        self.__session = None
        self.__config_reader = None

    def __before_request_checks(self) -> None:

        self.check_config_loaded()
        self.check_session_created()

    @staticmethod
    def formatted_str_as_int(string: str) -> int:

        # Trim and remove any commas
        string = string.strip()
        string = string.replace(",", "")

        return int(string)

    @staticmethod
    def validate_request_template(template: dict) -> bool:

        list_of_expected_keys = ["api", "endpoint", "url", "host", "method", "payloadTemplate"]
        list_of_actual_keys =template.keys()

        list_of_missing_keys = [key for key in list_of_expected_keys if key not in list_of_actual_keys]

        if len(list_of_missing_keys) > 0:
            return False
        else:
            return True

    def validate_response_status(self, response: requests.Response, error: bool = True) -> bool:
        """Validate the response's status

        Args:
            response (requests.Response): A Response object.
            error (bool, optional): Should an exception be raised if the response has an unsuccessful status code. Defaults to True.

        Raises:
            self.Exceptions.UnsuccessfulRequest: The server responded with a status code different from a successfull response and the error arg is set to True.

        Returns:
            bool: The server responded ok?
        """

        if response.status_code >= 400:
            msg = "The server responded with an HTTP status code different from a successful response ({0})".format(response.status_code)
            if error:
                raise self.Exceptions.UnsuccessfulRequest(msg)
            else:
                self.logger.warning(msg)
                return False

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
        """Create a logger object for the current class instance

        Args:
            level (int): logging level.
            name (str, optional): Name of the logger. Defaults to "Scrapper.logger".
            format (str, optional): String template for the logger message formatter. Defaults to "%(asctime)s | %(levelname)7s @ %(filename)s : %(message)s".
            date_format (str, optional): String template for the datetime formatter used in the logger.. Defaults to "%Y-%m-%d %H:%M:%S".
        """

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
        """Create a requests session.
        """

        self.logger.info("Creating new requests session...")
        self.__session = requests.Session()
        self.__session_created = True
        self.logger.info("Session created!")

    def send_request(self, method:str, url:str, **kwargs) -> requests.Response:
        """Send a request.

        This method sends an HTTP request using the specified method and URL. 
        This method is a wrapper around `Scrapper.session.request(...)`, which itself is a wrapper around `Session.request(...)` from the `requests` package.

        Additional arguments can be passed to `Session.request(...)`.

        Args:
            method (str): HTTP method to be used.
            url (str): Target URL of the request.

        Returns:
            requests.Response: Response object generated by the request.
        """

        self.logger.info("Sending {0} request to {1}...".format(method, url))
        
        self.check_session_created()

        r = self.session.request(method = method, url = url, **kwargs)

        return r

    def send_request_from_template(self, template: dict, payload: dict = None) -> requests.Response:
        """Send a request using a request template

        This function is a wrapper around `Scrapper.send_request(...)` that allows users to send an HTTP request using a request template.
        Request templates contain a predefined url, host, method, and payload (used as the data argument in `Session.request(...)`).

        Args:
            template (dict): A request template (as a python dict).
            payload (dict, optional): A python dict used to update the template's payload object. Defaults to None.

        Raises:
            self.Exceptions.InvalidTemplate: If the user suplied an invalid template.

        Returns:
            requests.Response: Response object generated by the request.
        """
        
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
        """Initializes the Scrapper's request session

        The public version of Mexico's National Registry of Missing and Untraceable Persons redirects to a welcome message and disclaimer 
        when accessing for the first time to the app. To avoid the redirect, the Scrapper sends an HTTP GET request to the app's index and the
        dahsboard home, in order to get a session cookie. This session cookie is necessary in subsequent requests to the page in order to signal
        the server that we're recurrent users.

        """
        
        self.logger.info("Initializing requests session...")
        self.check_session_created()

        template_index = self.get_request_template(api_name = "dashboard", end_point = "index")
        template_home = self.get_request_template(api_name = "dashboard", end_point = "home")

        # Send request to index page
        self.logger.info("Requesting dashboard index...")
        self.send_request_from_template(template_index)
        # Send request to home page
        self.logger.info("Requesting dashboard home...")
        self.send_request_from_template(template_home)

        self.logger.info("Request session initialized!")

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

    def get_states_catalogue(self) -> list:

        self.logger.info("Requesting states catalogue...")
        self.__before_request_checks()

        template = self.get_request_template(api_name = "catalogue", end_point = "states")
        
        r = self.send_request_from_template(template)

        # Get JSON
        r_content_as_dict = r.json()

        # Clean 
        list_of_states = []
        
        for obj in r_content_as_dict:
            id = obj["Value"]
            name = obj["Text"]

            name = "All" if name == "--TODOS--" else name

            list_of_states.append({"id": id, "name": name})

        return list_of_states

    def get_municipalities_catalogue(self, state_id: str) -> list:
        
        self.logger.info("Requesting municipalities catalogue for the state id {0}...".format(state_id))
        self.__before_request_checks()

        template = self.get_request_template(api_name = "catalogue", end_point = "municipalities")
        
        r = self.send_request_from_template(template, payload = {"idEstado": state_id})

        # Get JSON
        r_content_as_dict = r.json()

        # Clean 
        list_of_municipalities = []
        
        for obj in r_content_as_dict:
            id = obj["Value"]
            name = obj["Text"]

            name = "All" if name == "--TODOS--" else name

            list_of_municipalities.append({"id": id, "name": name})

        return list_of_municipalities

    def get_neighborhood_catalogue(self, state_id: str, mun_id: str):
        
        self.logger.info("Requesting neighborhood catalogue for the state id {0} and municipality id {1}...".format(state_id, mun_id))
        self.__before_request_checks()

        template = self.get_request_template(api_name = "catalogue", end_point = "neighborhoods")
        
        r = self.send_request_from_template(template, payload = {"idEstado": state_id, "idMunicipio": mun_id})

        # Get JSON
        r_content_as_dict = r.json()

        # Clean 
        list_of_neighborhoods = []
        
        for obj in r_content_as_dict:
            id = obj["Value"]
            name = obj["Text"]

            name = "All" if name == "--TODOS--" else name

            list_of_neighborhoods.append({"id": id, "name": name})

        return list_of_neighborhoods


    def get_totals(self, state_id: str = "0", mun_id: str = "0", neighborhood_id: str = "0", date_start: str = "", date_ent: str = "", **kwargs) -> dict:
        pass

    def get_missing_by_neighborhood(self, state_id: str, mun_id: str, neighborhood_id: str = "0", **kwargs) -> dict:
        pass
