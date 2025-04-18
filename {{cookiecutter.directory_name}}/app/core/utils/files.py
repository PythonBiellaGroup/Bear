import os
import re
import shutil

import yaml
from loguru import logger


def check_if_file_exists(file: str) -> bool:
    """Check if a file exist in a specific path.

    Args:
        file (str): the file path or name

    Returns:
        (bool): True if the file exist, False otherwise
    """
    if os.path.exists(file) and os.path.isfile(file):
        return True

    return False


def init_folder(path: str, output=False) -> bool:  # noqa
    """Initialize a folder (create if not exist).

    Args:
        path (str): path of the folder
        output (bool, optional): if you want to see the path of the folder. Defaults to False.

    Returns:
        (bool): True if the folder is created, False otherwise
    """
    try:
        os.mkdir(path)
        return True
    except Exception as message:
        if output:
            print(f"{path} already exists: {message}")
        return False


def remove_folder(folder_path: str, force: bool = False) -> bool:  # noqa
    """Remove a folder if exist, if not exist return false.

    If you want remove folders not empty you have to use force=True, but be careful because can be really dangerous!

    Args:
        folder_path (str): path of the folder
        force (bool, optional): if you want to remove folders not empty. Defaults to False.

    Returns:
        (bool): True if the folder is removed, False otherwise
    """
    # Check if the folder exists
    if os.path.exists(folder_path):
        if force:
            # forcing the removal (can be dangerous)
            # this can help to remove folder not empty
            shutil.rmtree(folder_path, ignore_errors=True)
        else:
            # If it exists, remove it (safe remove)
            os.rmdir(folder_path)
        print(f"Removed folder at {folder_path}")
        return True

    return False


# Yaml Library and functions
def get_folder_path(custom_path: str = "", force_creation: bool = False) -> str:  # noqa
    """Get the folder absolute path starting from a relative path of your python launch file.

    This function is os independent, so it's possibile to use everywherre

    Args:
        custom_path (str, optional): The relative path of your path search. Defaults to "".
        force_creation (bool, optional): if the path doesn't exist, force the creation of the folder. Defaults to False.

    Returns:
        str: The absolute path you want to search
    """
    if custom_path == "" or custom_path is None:
        basepath = os.path.abspath("")
    else:
        basepath = os.path.abspath(custom_path)

    # Check if the folder exist, if not exit you can create with a flag
    if not os.path.exists(basepath):
        logger.error("WARNING: Path doesn't exist")
        if force_creation:
            logger.debug("Force creation folder")
            try:
                os.makedirs(basepath)
            except Exception as message:
                logger.error(f"Impossible to create the folder: {message}")

    logger.debug(f"PATH: {basepath}, force creation: {force_creation}")
    return basepath


def search_path(to_path: str, filename: str) -> str:
    """Search a specific filename into a folder path.

    Args:
        to_path (str): path where you want to search
        filename (str): name of the file

    Returns:
        str: the relative path where the file is
    """
    try:
        if to_path == "" or to_path is None:
            to_path = get_folder_path("./")

        if filename == "" or filename is None:
            filename = "result.yml"

        if re.search(r"yml", filename) is False:
            filename = filename + ".yml"

        return os.path.join(to_path, filename)

    except Exception as message:
        logger.error(f"Path: {to_path}, or filename: {filename} not found: {message}")
        return ""


def read_yaml(file_path: str, filename: str = "") -> dict:
    """Read a yaml file from disk.

    Args:
        file_path (str): path where you want to load
        filename (str, optional): Name of the file you want to load. Defaults to "".

    Returns:
        dict: The dictionary readed from the yaml file
    """
    file_path = search_path(file_path, filename)

    try:
        with open(file_path) as file:
            data = yaml.safe_load(file)
            file.close()
        logger.debug(f"Yaml file: {filename} loaded")
        return data

    except Exception as message:
        logger.error(f"Impossible to load the file: {filename} with path: {file_path}")
        logger.error(f"Error: {message}")
        return {}


def write_yaml(to_path: str, filename: str, obj_save: object) -> bool:
    """Write some properties to generic yaml file.

    Args:
        to_path (str): the path you want to write the file
        filename (str): the name of the file
        obj_save (obj): the python object you want to save (for example a dictionary)

    Returns:
        (bool) a boolean value with success or insuccess)
    """
    file_path = search_path(to_path, filename)

    try:
        with open(file_path, "w") as file:
            yaml.dump(obj_save, file)
        file.close()
        logger.debug(f"File successfully written to: {file_path}")
        return True

    except Exception as message:
        logger.error(f"Impossible to write the file: {message}")
        return False
