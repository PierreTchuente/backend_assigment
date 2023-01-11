import logging
import os
import threading
from configparser import ConfigParser


class Config:
    """
    This a basic configuration class. This class is singleton.
    any configuration depending on a specific environment can
    be added on the corresponding ini file.
    """

    _logger = None
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Config, cls).__new__(cls)
                    cls._instance.logger = logging.getLogger(__name__)
                    cls._instance.config_parser = ConfigParser()
        return cls._instance

    def configure(self):
        with self.__class__._lock:
            self._instance._configure()

    @classmethod
    def get_instance(cls):
        """
        :return: return an instance of Config.
        """
        if cls._instance is None:
            cls._instance = Config()
            cls._instance.configure()
        return cls._instance

    def _configure(self):
        """
        The CONFIG_FILE to use for this test should be set as an
        env variable.
        """
        environment = os.environ.get("CONFIG_FILE") or "development"
        config_file = os.path.join(
            os.path.dirname(__file__),
            f"{os.path.dirname(os.path.abspath(__file__))}/config_files/"
            f"{environment}.ini",
        )
        if not os.path.exists(config_file):
            raise ValueError(f"file {config_file} does not exit")

        self._instance.config_parser.read(config_file)
        self._instance.logger.info(
            f"section keys {self._instance.config_parser.sections()}"
        )
        self._instance.logger.info(f"Using config file {config_file}")

    def _configure_logging(self):
        """
        Basic logger configuration
        """
        if self._instance._logger:
            return
        logging.basicConfig(level="INFO")
        self._instance._logger = logging.getLogger("service_api")

    @staticmethod
    def get_logger():
        config = Config.get_instance()
        config._configure_logging()
        return config._logger

    @staticmethod
    def get_db_setting():
        config = Config.get_instance()
        return {
            "database": config.config_parser.get("db_setting", "database"),
            "user": config.config_parser.get("db_setting", "user"),
            "password": config.config_parser.get("db_setting", "password"),
            "host": config.config_parser.get("db_setting", "host"),
            "raise_on_warnings": bool(
                config.config_parser.get("db_setting", "raise_on_warnings")
            ),
        }
