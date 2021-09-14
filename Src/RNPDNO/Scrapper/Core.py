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

        pass