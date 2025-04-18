import logging
import time

from loguru import logger


class Profiler:
    """Logging proxy that injects to duration since object creation."""

    def __init__(self):
        self.start = time.time()
        self.last = 0

    def stamp(self, message: str) -> tuple[float, str]:
        """Stamp message with elapsed time."""
        seconds = time.time() - self.start
        return seconds, f"{message} @{seconds:.3f}s"

    def log(self, level: int, message: str, *args: list, **kwds: dict):
        """Generic log call, adds elapsed time to message and extra."""
        duration, message = self.stamp(message)
        time_delta = duration - self.last
        self.last = duration
        logger.log(level, message, *args, **kwds, duration=duration, time_delta=time_delta)

    def debug(self, message: str, *args: list, **kwds: dict):
        """Debug log with elapsed time in message and extra."""
        self.log(logging.DEBUG, message, *args, **kwds)

    def info(self, message: str, *args: list, **kwds: dict):
        """Info log with elapsed time in message and extra."""
        self.log(logging.INFO, message, *args, **kwds)

    def warn(self, message: str, *args: list, **kwds: dict):
        """Warn log with elapsed time in message and extra."""
        self.log(logging.WARN, message, *args, **kwds)

    def error(self, message: str, *args: list, **kwds: dict):
        """Error log with elapsed time in message and extra."""
        self.log(logging.ERROR, message, *args, **kwds)


def send_ping(email: str, message: str):
    """Test function to send a dummy ping for testing purpose."""
    return f"You send to: {email} the message: {message}"
