import os
import sys

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggerSettings(BaseSettings):
    """Logger configuration settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    APP_NAME: str = "bear"
    LOG_VERBOSITY: str = "DEBUG"
    LOG_ROTATION_SIZE: str = "100MB"
    LOG_RETENTION: str = "30 days"
    LOG_FILE_NAME: str = APP_NAME + "_{time:DD-MM-YYYY}.log"
    LOG_FORMAT: str = "{level}\t| {time:DD-MM-YYYY:HH:mm:ss!UTC} utc | {file}:{module}:{line} | {message}"
    REPO_PATH: str = os.path.abspath(".")  # Set REPO_PATH to the current directory
    LOG_FOLDER: str = os.path.join(REPO_PATH, "logs")  # Default log folder
    LOG_FILE_PATH: str = os.path.join(LOG_FOLDER, LOG_FILE_NAME)
    PROFILE: bool = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.LOG_FOLDER = os.path.join(self.REPO_PATH, "logs")  # Dynamically set LOG_FOLDER
        self.LOG_FILE_PATH = os.path.join(self.LOG_FOLDER, self.LOG_FILE_NAME)  # Update LOG_FILE_PATH
        self.APP_NAME = self.APP_NAME
        self.LOG_FILE_NAME = self.APP_NAME + "_{time:D-M-YY}.log"

    def setup_logger(self):
        """Configure the logger."""
        logger.remove()  # Remove previous handlers
        logger.add(
            sink=sys.stderr,
            colorize=True,
            format=self.LOG_FORMAT,
            level=self.LOG_VERBOSITY,
            serialize=False,
            catch=True,
            backtrace=False,
            diagnose=False,
        )
        logger.add(
            sink=self.LOG_FILE_PATH,
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
