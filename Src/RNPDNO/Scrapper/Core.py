import requests

class Scrapper:

    class Exceptions:

        class ConfigNotLoaded(Exception):
            pass

        class TemplateNotFound(Exception):
            pass

        class MultipleTemplatesFound(Exception):
            pass

    def __init__(self) -> None:
        
        self.__config_loaded = False

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

        pass