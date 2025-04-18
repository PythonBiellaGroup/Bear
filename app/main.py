from loguru import logger

from app.core.config import settings
from app.domain.utils.manager import convert_numbers, logic_test

if __name__ == "__main__":
    logger.info(f"Welcome to: {settings.APP_NAME}")

    message = "Ciao JeyDi!"
    numbers = [1, 2, 3, 4, 5, 6]

    new_message = logic_test(message)
    result = convert_numbers(numbers)
    logger.info(f"Message: {new_message}, with numbers: {numbers}")
