import logging
import logging.handlers
import os

import ecs_logging
from loguru import logger
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings class for application settings and secrets management.

    Official documentation on pydantic settings management:
    - https://pydantic-docs.helpmanual.io/usage/settings/
    """

    # Set the application variables
    APP_NAME: str = "Test"
    # if you want to test gunicorn the below environment variabile must be False
    DEBUG_MODE: str = "True"
    VERBOSITY: str = "DEBUG"

    # Logger
    LOG_VERBOSITY: str = "INFO"
    LOG_ROTATION_SIZE: str = "100MB"
    LOG_RETENTION: str = "30 days"
    LOG_FILE_NAME: str = "./logs/jf_{time:D-M-YY}.log"
    LOG_FORMAT: str = "{time:HH:mm:ss!UTC}\t|\t{file}:{module}:{line}\t|\t{message}"
    ECS_LOG_PATH: str = f"./logs/elastic-{os.getpid()}.log"

    def _setup_logger(self):
        # logger.remove()  # to remove default logging to StdErr
        logger.add(
            self.LOG_FILE_NAME,
            rotation=self.LOG_ROTATION_SIZE,
            retention=self.LOG_RETENTION,
            colorize=True,
            format=self.LOG_FORMAT,
            level=self.LOG_VERBOSITY,
            serialize=False,
            catch=True,
            backtrace=False,
            diagnose=False,
            encoding="utf8",
        )

        # Proxy loguru logs also to logging logger.
        # The ecs logging formats all logs from the python logging system for elastic.
        # It could be configured to read logs directly from loguru, but in that case it
        # would miss all parts of the system that log directly to the python logging
        # system.
        class PropagateHandler(logging.Handler):
            def emit(self, record):
                logging.getLogger(record.name).handle(record)

        logger.add(PropagateHandler(), format="{message}")

        # Add ECS rotating files sink
        pylogger = logging.getLogger()
        ecs_handler = logging.handlers.RotatingFileHandler(
            self.ECS_LOG_PATH,
            maxBytes=100_000_000,
            backupCount=2,
            encoding="utf8",
        )
        ecs_handler.setFormatter(
            ecs_logging.StdlibFormatter(
                extra={
                    "release": self.RELEASE,
                    "project": self.PROJECT_NAME,
                }
            )
        )
        ecs_handler.setLevel(logging.INFO)
        pylogger.addHandler(ecs_handler)

        return True

    # Application Path
    APP_PATH: str = os.path.abspath(".")
    CONFIG_PATH: str = os.path.join(APP_PATH, "app", "config")
    DATA_PATH: str = os.path.join(APP_PATH, "app", "data")


def get_settings() -> Settings:
    """Generate and get the settings."""
    try:
        settings = Settings()
        settings._setup_logger()
        return settings
    except Exception as message:
        logger.error(f"Error: impossible to get the settings: {message}")
        return None


settings = get_settings()
