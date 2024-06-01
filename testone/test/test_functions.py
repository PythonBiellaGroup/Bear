from typing import List

import pytest
from loguru import logger

from app.src.core.manager import convert_numbers, logic_test


@pytest.mark.functions
def test_logic_base():
    """Test the logic_base function.

    This function tests the logic_base function by checking if the output message is equal to "CIAO JEYDI!".
    """
    logger.debug("test logic base con messaggio")
    message = "Ciao PythonBiellaGroup!"
    message = logic_test(message)
    assert message == "CIAO PythonBiellaGroup!"


@pytest.mark.core
def test_entities():
    """Test the entities function.

    This function tests the `convert_numbers` function by passing a list of numbers and
    asserting that the result is a list and the expected output is returned.

    """
    logger.debug("test entities base con lista di numeri")
    numbers = [1, 2, 3, 4, 5]
    result = convert_numbers(numbers)
    assert result is List
    assert result == [25]


if __name__ == "__main__":
    logger.info("test di esempio")

    test_logic_base()
    test_entities()
