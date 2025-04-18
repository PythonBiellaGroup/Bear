import importlib
import inspect
from typing import Any, Callable

import loguru as logger


def load_class(path_to_module: str, class_name: str) -> Any:
    """Load a specific class using simply the path of the module and the class name.

    This function use importlib to simplify the loading of a class.

    Args:
        path_to_module (str): the python path to the module
        class_name (str): the name of the class you want to load

    Returns:
        (Any): the class loaded
    """
    module = importlib.import_module(path_to_module)
    return getattr(module, class_name)


def get_default_args(func: Callable):
    """Get the default arguments of a function.

    Args:
        func (Callable): the function you want to get the default arguments
    Returns:
        (dict): the default arguments of the function
    """
    signature = inspect.signature(func)
    return {k: v.default for k, v in signature.parameters.items() if v.default is not inspect.Parameter.empty}


# String to bool
def string_to_bool(text: str) -> bool:
    """Convert input string into booleean.

    Args:
        text: Input string

    Raises:
        Unrecognized string

    Returns:
        result (boolean): True or False
    """
    if text.lower().strip() in [
        "true",
        "1",
        "t",
        "y",
        "yes",
        "yeah",
        "yup",
        "certainly",
        "uh-huh",
    ]:
        result = True
    elif text.lower().strip() in [
        "false",
        "wrong",
        "no",
        "0",
        "n",
        "nah",
        "nope",
        "nah-nah",
    ]:
        result = False
    else:
        message = "Could not convert string to bool"
        logger.error(message)
        raise ValueError(message)

    return result
