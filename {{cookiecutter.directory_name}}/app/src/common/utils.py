import datetime as dt
import importlib
import json
import os
import re
from datetime import datetime
from typing import Any, Optional, Union
from loguru import logger

import numpy as np
import pandas as pd
import unidecode
import yaml


def profiling_api(
    description: str,
    start: dt.datetime,
    message_type: str = "info",
    user: str = "system",
) -> None:
    """
    Profile the API by checking and savings the logs:
    - description: description of the API
    - start: start time of the API (to calc how much time it took)
    - message_type: type of message (info, warning, error)
    - user: user who made the API call
    """
    difference = dt.datetime.now() - start
    seconds = difference.total_seconds()
    # milliseconds = seconds * 1000
    message = (
        description
        + " : "
        + str(user)
        + " : "
        + str(seconds)
        + " seconds"
        # + str(milliseconds)
        # + " milliseconds"
    )
    message_type = message_type.lower().strip()
    if message_type == "info":
        logger.info(message)
    if message_type == "debug":
        logger.debug(message)
    if message_type == "error":
        logger.error(message)


def remove_dict_none_values(dictionary: dict) -> list:
    """Remove dictionary keys whose value is None

    Args:
        dictionary [dict]: dictionary to clean

    Returns:
        a list of keys without none values
    """
    return list(map(dictionary.pop, [i for i in dictionary if dictionary[i] is None]))


def listfloat(a: list) -> list:
    """Given a list in input of string expressed as numbers, transform the number inside the list in float and return the list transformed.

    Args:
        a: list of string (e.g. ['1', '2', '3'])

    Returns:
        the list transformed
    """
    if "" in a:
        a.remove("")
    return [float(x) for x in a]


def custom_int_parsing(value: Union[str, list]) -> Any:
    """Custom string to int parsing.

    You can pass a single string value or a list of string.
    If the input string it's empty or not valid, return None instead broken the code.

    Args:
        value (Union[str, list]): A single string value or a list of strings

    Returns:
        list: converted values.
    """
    if isinstance(value, str):
        value = [value]
    result = []
    for i in value:
        r = re.findall(r"\D", i)
        if len(r) == 0 and len(i) > 0:
            e = int(i)
            result.append(e)

    if len(result) == 1:
        return result[0]
    elif len(result) == 0:
        return None
    else:
        return result


def write_log(message: str) -> None:
    """Write a simple log

    Args:
        message (str): the message you want to write
    """
    with open("log.txt", mode="a") as log:
        log.write(message)


# Conversions
def underscore_to_camelcase(text: str) -> str:
    """Converts a name or test with underscore to camelcase

    Args:
        text (str): string with underscore
    Returns:
        str: string with camelcase
    """
    return "".join(x.capitalize() for x in text.split("_"))


def millis2date(ms: int) -> Optional[dt.datetime]:
    """Converts a number of milliseconds elapsed since January 1st, 1970 00:00:00 UTC to a datatime object (ms=0 <=> January 1st, 1970 00:00:00 UTC)

    Args:
        ms (int): number of ms elapsed since January 1, 1970 00:00:00 UTC

    Returns:
        dt.datetime: datetime corresponding to the given number of milliseconds
    """
    return dt.datetime.fromtimestamp(ms / 1000.0) if pd.notnull(ms) else None


def date2millis(date: str, date_format: str = "%Y-%m-%d %H:%M:%S") -> Optional[float]:
    """Converts a date given as a string with given format to a number of millisecond elapsed since January 1st, 1970 00:00:00 UTC
    Args:
        date (str): string containing the date e.g. "2021-12-13 00:00:00"
        date_format (str): what is the format of the date? see datetime documentation for details https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes. Defaults to "%Y-%m-%d %H:%M:%S".
    Returns:
        typing.Union[dt.datetime, None]: datetime corresponding to the given number of milliseconds or None if date is None.
    """
    return (
        dt.datetime.strptime(date, date_format).timestamp() * 1000
        if pd.notnull(date)
        else None
    )


def parse_date(date: str, date_format: str = "%Y-%m-%d") -> dt.date:
    """Converts the given date to datetime object using the given date_format

        Args:
            date (str): the date to convert e.g. "2022-12-13"
            date_format (str): what is the format of the date? see datetime documentation for details https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes. Defaults to "%Y-%m-%d %H:%M:%S".
    . Defaults to "%Y-%m-%d".

        Returns:
            dt.datetime: the given date converted as a datetime object
    """
    return dt.datetime.strptime(date, date_format).date()


def parse_datetime(date: str, date_format: str = "%Y-%M-%D %H:%M:%S") -> dt.datetime:
    return datetime.strptime(date, date_format)


def date_to_string(date: dt.date, date_format: str = "%Y-%m-%d") -> Union[float, str]:
    """Returns a string representation of a datetime object

    Args:
        date: dt.datetime the date
        date_format: what is the format of the date? see datetime documentation for details https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes. Defaults to "%Y-%m-%d".

    Returns:
        Union[float, str]: the string associated with the given date in the given format
    """
    return date.strftime(date_format) if not pd.isnull(date) else np.nan


def datetime_to_string(
    date: dt.datetime, date_format: str = "%Y-%m-%d %H:%M:%S"
) -> Union[float, str]:
    """Returns a string representation of a datetime object

    Args:
        date: dt.datetime the date
        date_format: what is the format of the date? see datetime documentation for details https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        Union[float, str]: the string associated with the given date in the given format
    """
    if not pd.isnull(date):
        return date.strftime(date_format)
    else:
        return np.nan


def string_to_date(
    x: Union[str, dt.date, Any], date_format: str = "%Y-%m-%d %H:%M:%S"
) -> Union[float, dt.date]:
    """Convert a string to a datetime object, specyfing the format of the string

    Args:
        x: _description_
        date_format: _description_. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        _description_
    """
    if isinstance(x, str):
        return (
            dt.datetime.strptime(x, date_format).date() if not pd.isnull(x) else np.nan
        )
    elif isinstance(x, dt.date):
        return x
    else:
        return np.nan


def parsedates(column: pd.Series) -> pd.Series:
    """Convert Series from string to date

    Args:
        column (pd.Series): date string column

    Returns:
        [pd.Series]: datetime column
    """
    column_stripped = column.astype(str).str.strip()
    return pd.to_datetime(column_stripped, format="%d-%b-%y")


def parsedates_withhour(column: pd.Series) -> pd.Series:
    """Convert Series from string to date

    Args:
        column (pd.Series): date string column

    Returns:
        [pd.Series]: datetime column
    """
    column_stripped = column.astype(str).str.strip()
    try:
        return pd.to_datetime(column_stripped, format="%d/%m/%Y %H:%M:%S")
    except Exception as message:
        logger.warning(f"date {column.name} has wrong format! {message}")
        return pd.to_datetime(
            column_stripped, format="%d/%m/%Y %H:%M:%S", errors="coerce"
        )


def string_contains(text: str, words: str) -> bool:
    """Check if a string contain a specific word

    Args:
        x (str): your string with the text
        words (str): the word or the text you want to search

    Returns:
        (bool) if the words it's present in the x string
    """
    return any([w in text for w in words])


def series_cutstring(column: pd.Series, stop: int = 3) -> pd.Series:
    """Cut a string to a specific length

    Args:
        column (pd.Series): the string column
        stop (int): when you need to stop to cut the string (number of chars) . Defaults to 3.

    Returns:
        the string cut to the given length
    """
    return column.astype(str).str.slice(stop=stop)


def as_list(x: Any) -> list:
    """Check if a variable is a list or not
    If not return the variable as a list

    Args:
        x: the variable to check

    Returns:
        a list
    """
    if isinstance(x, list):
        return x
    else:
        return [x]


def remove_columns(dataset: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Remove columns from a pandas dataframe

    Args:
        dataset (pd.DataFrame): pandas dataframe as input
        cols (list of strings): list of columns you want to remove

    Returns:
        the dataset without the columns
    """
    if isinstance(cols, str):
        cols = [cols]
    cols = [c for c in cols if c in dataset.columns]
    dataset = dataset.drop(cols, axis=1)  # type: ignore
    return dataset


def keep_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Keep only the columns you want in a pandas dataframe and remove everything else

    Args:
        df (pd.DataFrame): input pandas dataframe
        cols (list): the list of columns you want to keep inside the pandas dataframe

    Returns:
        (pd.DataFrame): the dataframe with only the columns you want to keep
    """
    if isinstance(cols, str):
        cols = [cols]
    cols = [c for c in cols if c in df.columns]
    df = df.loc[:, cols]  # type: ignore
    return df


def save_dict_to_json(d: dict, file: str) -> str:
    """Save a dictionary to a json file

    Args:
        d (dict): the dictionary to save
        file (str): the file path or filename where you want to save the dictionary

    Returns:
        (str): the filepath of the saved file
    """
    with open(file, "w") as fp:
        json.dump(d, fp, sort_keys=True, indent=4)
    return file


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


# Check Dataframe Utility function
def check_df(dataframe: pd.DataFrame, sample: bool = False) -> None:
    """Get the informations about a pandas dataframe (shape, columns, dtypes, ...).
    This function use the logger to print the informations (with an "info" level)

    Args:
        dataframe (pd.DataFrame): the pandas dataframe you want to check
        sample (bool): If you want also a sample of top 5 rows. Defaults to False.
    """
    logger.info(
        f"Dataframe Shape: {dataframe.shape} with rows: {dataframe.shape[0]} and columns: {dataframe.shape[1]}"
    )
    logger.info(f"\nDF Columns: \n{list(dataframe.columns)}")
    if sample:
        logger.info(f"\nData:\n{dataframe.head(5)}")


# FILES
def check_if_file_exists(file: str) -> bool:
    """Check if a file exist in a specific path

    Args:
        file (str): the file path or name

    Returns:
        (bool): True if the file exist, False otherwise
    """
    if os.path.exists(file) and os.path.isfile(file):
        return True
    else:
        return False


def remove_special_characters(s: str) -> str:
    """Remove special characters from a string

    Args:
        s (str): the string you want to fix

    Returns:
        (str): the string without special characters
    """
    return (
        unidecode.unidecode(s)
        .replace("/", "_")
        .replace("-", "_")
        .replace("(", "_")
        .replace(")", "_")
        .replace(".", "_")
        .replace(" ", "_")
        .replace("&", "and")
        .replace("'", "")
        .replace("__", "_")
        .replace("___", "_")
        .lower()
    )


# Yaml Library and functions
def get_folder_path(custom_path: str = "", force_creation: bool = False) -> str:
    """Get the folder absolute path starting from a relative path of your python launch file.
    This function is os independent, so it's possibile to use everywherre

    Args:
        custom_path (str, optional): The relative path of your path search. Defaults to "".
        force_creation (bool, optional): if the path doesn't exist, force the creation of the folder. Defaults to False.

    Returns:
        str: The absolute path you want to search
    """

    if custom_path == "" or custom_path is None:
        BASEPATH = os.path.abspath("")
    else:
        BASEPATH = os.path.abspath(custom_path)

    # Check if the folder exist, if not exit you can create with a flag
    if not os.path.exists(BASEPATH):
        logger.error("WARNING: Path doesn't exist")
        if force_creation:
            logger.debug("Force creation folder")
            try:
                os.makedirs(BASEPATH)
            except Exception as message:
                logger.error(f"Impossible to create the folder: {message}")

    logger.debug(f"PATH: {BASEPATH}, force creation: {force_creation}")
    return BASEPATH


def checkpath(to_path: str, filename: str) -> str:
    """
    Check path and filename
    Search a specific filename into a folder path

    Args:
        to_path (str): path where you want to search
        filename (str): filename

    Returns:
        str: the path where the file is
    """
    try:
        if to_path == "" or to_path is None:
            to_path = get_folder_path("./")

        if filename == "" or filename is None:
            filename = "result.yml"

        if re.search(r"yml", filename) is False:
            filename = filename + ".yml"

        file_path = os.path.join(to_path, filename)
        return file_path

    except Exception as message:
        logger.error(f"Path: {to_path}, or filename: {filename} not found: {message}")
        return ""


def read_yaml(file_path: str, filename: str = "") -> dict:
    """Read a yaml file from disk

    Args:
        file_path (str): path where you want to load
        filename (str, optional): Name of the file you want to load. Defaults to "".

    Returns:
        dict: The dictionary readed from the yaml file
    """
    file_path = checkpath(file_path, filename)

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


def write_dataset_yaml(
    to_path: str = "", filename: str = "", dataset: pd.DataFrame = None
) -> bool:
    """Write a pandas dataset to yaml

    Args:
        to_path (str, optional): Path where you want to save the yaml file. Defaults to "".
        filename (str, optional): Name of the file to use. Defaults to "".
        dataset (pd.DataFrame, optional): Pandas dataframe to save. Defaults to None.

    Returns:
        bool: If the
    """
    file_path = checkpath(to_path, filename)

    if not isinstance(dataset, pd.DataFrame):
        logger.error("Please use a Pandas dataframe with write_dataset_yaml function")
        return False

    try:
        with open(file_path, "w") as file:
            yaml.dump(dataset, file)
        file.close()
        logger.debug(f"File successfully write to: {file_path}")
        return True

    except Exception as message:
        logger.error(f"Impossible to write the file: {message}")
        return False


def write_yaml(to_path: str, filename: str, obj_save: object) -> bool:
    """Write some properties to generic yaml file

    Args:
        to_path (str): the path you want to write the file
        filename (str): the name of the file
        obj_save (obj): the python object you want to save (for example a dictionary)

    Returns:
        (bool) a boolean value with success or insuccess)
    """
    file_path = checkpath(to_path, filename)

    try:
        with open(file_path, "w") as file:
            yaml.dump(obj_save, file)
        file.close()
        logger.debug(f"File successfully written to: {file_path}")
        return True

    except Exception as message:
        logger.error(f"Impossible to write the file: {message}")
        return False


def last_of_month(date: dt.date) -> dt.date:
    """Get the last day of month from a datetime date

    Args:
        date (date): Input date to get the last day of month

    Returns:
        date: Last day of month
    """
    d = dt.date(
        date.year + int(date.month / 12), date.month % 12 + 1, 1
    ) - dt.timedelta(days=1)

    return d


def first_of_month(date: dt.date) -> dt.date:
    """Get the first day of month from a datetime date

    Args:
        date (date): Input date to get the first day of month

    Returns:
        date: First day of month
    """
    d = date.replace(day=1)

    return d
