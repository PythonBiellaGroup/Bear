import datetime as dt
import hashlib
import html
import io
import json
import re
from typing import Any, Optional, Union

import html2text
import numpy as np
import pandas as pd
import unidecode
from bs4 import BeautifulSoup
from flatdict import FlatDict
from loguru import logger


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


# Conversions
def underscore_to_camelcase(text: str) -> str:
    """Converts a name or test with underscore to camelcase.

    Args:
        text (str): string with underscore
    Returns:
        str: string with camelcase
    """
    return "".join(x.capitalize() for x in text.split("_"))


def millis2date(ms: int, force_utc: bool = True) -> Optional[dt.datetime]:  # noqa
    """Converts a number of milliseconds elapsed since January 1st, 1970 00:00:00 UTC to a datatime object (ms=0 <=> January 1st, 1970 00:00:00 UTC).

    Args:
        ms (int): number of ms elapsed since January 1, 1970 00:00:00 UTC
        force_utc (bool): if True, the datetime object is forced to be in UTC timezone. Defaults to True.

    Returns:
        dt.datetime: native datetime corresponding to the given number of milliseconds
    """
    if not pd.notnull(ms):
        return None

    result = dt.datetime.fromtimestamp(ms / 1000.0, tz=dt.timezone.utc)

    if not force_utc:
        # This changes the numerical values
        result = result.astimezone(tz=None)

    # This just strips the timezone info making it a naive datetime
    return result.replace(tzinfo=None)


def date2millis(date: str, date_format: str = "%Y-%m-%d %H:%M:%S", force_utc: bool = True) -> Optional[float]:  # noqa
    """Converts a date given as a string with given format to a number of millisecond elapsed since January 1st, 1970 00:00:00 UTC.

    Args:
        date (str): string containing the date e.g. "2021-12-13 00:00:00"
        date_format (str): what is the format of the date? see datetime documentation for details https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        typing.Optional[float]: float corresponding to the given number of milliseconds or None if date is None.
    """
    if not pd.notnull(date):
        return None

    date = dt.datetime.strptime(date, date_format).replace(tzinfo=dt.timezone.utc)
    if force_utc:
        date = date.replace(tzinfo=dt.timezone.utc)

    return date.timestamp() * 1000.0


def parse_date(date: str, date_format: str = "%Y-%m-%d") -> dt.date:
    """Converts the given date to datetime object using the given date_format.

    Args:
        date (str): the date to convert e.g. "2022-12-13"
        date_format (str): what is the format of the date? see datetime documentation for details https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes. Defaults to "%Y-%m-%d %H:%M:%S".
    . Defaults to "%Y-%m-%d".

    Returns:
        dt.datetime: the given date converted as a datetime object
    """
    return dt.datetime.strptime(date, date_format).replace(tzinfo=dt.timezone.utc).date()


def date_to_string(date: dt.datetime, date_format: str = "%Y-%m-%d") -> Union[float, str]:
    """Returns a string representation of a datetime object.

    Args:
        date: dt.datetime the date
        date_format: what is the format of the date? see datetime documentation for details https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes. Defaults to "%Y-%m-%d".

    Returns:
        Union[float, str]: the string associated with the given date in the given format
    """
    return date.strftime(date_format) if not pd.isnull(date) else np.nan


def datetime_to_string(date: dt.datetime, date_format: str = "%Y-%m-%d %H:%M:%S") -> Union[float, str]:
    """Returns a string representation of a datetime object.

    Args:
        date: dt.datetime the date
        date_format: what is the format of the date? see datetime documentation for details https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        Union[float, str]: the string associated with the given date in the given format
    """
    if not pd.isnull(date):
        return date.strftime(date_format)

    return np.nan


def string_to_date(x: Union[str, dt.date, Any], date_format: str = "%Y-%m-%d %H:%M:%S") -> Union[float, dt.date]:
    """Convert a string to a datetime object, specyfing the format of the string.

    Args:
        x: _description_
        date_format: _description_. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        _description_
    """
    if isinstance(x, str):
        return (
            dt.datetime.strptime(x, date_format).replace(tzinfo=dt.timezone.utc).date() if not pd.isnull(x) else np.nan
        )

    if isinstance(x, dt.date):
        return x

    return np.nan


def series_parsedates(column: pd.Series, format_date: str = "%Y-%m-%d") -> pd.Series:
    """Convert Pandas serie from string to date (in datetime date format not pandas data format).

    Args:
        column (pd.Series): date string column

    Returns:
        [pd.Series]: datetime column
    """
    column_stripped = column.astype(str).str.strip()
    df = pd.to_datetime(column_stripped, format=format_date)
    return df.apply(lambda x: x.date())


def series_parsedates_withhour(column: pd.Series, format_date: str = "%Y-%m-%d %H:%M:%S") -> pd.Series:
    """Convert Pandas serie from string to date.

    Args:
        column (pd.Series): date string column

    Returns:
        [pd.Series]: datetime column
    """
    column_stripped = column.astype(str).str.strip()
    try:
        return pd.to_datetime(column_stripped, format=format_date)
        # df = df.apply(lambda x: x.datetime())
        # return df
    except Exception as message:
        logger.warning(f"date {column.name} has wrong format! {message}, launching coercing (forcing)")
        return pd.to_datetime(column_stripped, format=format_date, errors="coerce")
        # df = df.apply(lambda x: x.datetime())
        # return df


def string_contains(text: str, words: str) -> bool:
    """Check if a string contain a specific word.

    Args:
        x (str): your string with the text
        words (str): the word or the text you want to search

    Returns:
        (bool) if the words it's present in the x string
    """
    return any(w in text for w in words)


def html_list_to_string(html_list: str) -> str:
    """Convert a html li string into a string separated by semicolon.

    Args:
        html_list (str): the html list to parse and to be converted into a string separated by ;

    Returns:
        str: the list with string separated by ;
    """
    if html_list is None:
        return ""
    keywords = html2text.html2text(html_list).replace("\n", "").replace("\n", "").split("*")
    keywords = [i.strip() for i in keywords]
    if "" in keywords:
        keywords.remove("")
    return " ; ".join(keywords)


def series_cutstring(column: pd.Series, stop: int = 3) -> pd.Series:
    """Cut a string to a specific length.

    Args:
        column (pd.Series): the string column
        stop (int): when you need to stop to cut the string (number of chars) . Defaults to 3.

    Returns:
        the string cut to the given length
    """
    return column.astype(str).str.slice(stop=stop)


def as_list(x: Any) -> list:
    """Check if a variable is a list or not.

    If not return the variable as a list

    Args:
        x: the variable to check

    Returns:
        a list
    """
    if isinstance(x, list):
        return x

    return [x]


def remove_special_characters(s: str, replace_char: str = "") -> str:
    """Remove special characters from a string to a specific replace char and lower the output string (stripping also the string by removing start and ending spaces).

    Args:
        s (str): the string you want to fix

    Returns:
        (str): the string without special characters
    """
    return (
        unidecode.unidecode(s)
        .replace("/", replace_char)
        .replace("-", replace_char)
        .replace("(", replace_char)
        .replace(")", replace_char)
        .replace(".", replace_char)
        .replace(" ", replace_char)
        .replace("&", replace_char)
        .replace("'", replace_char)
        .replace("__", replace_char)
        .replace("___", replace_char)
        .lower()
        .strip()
    )


def remove_non_en_chars(sentence: str) -> str:
    """Remove non english characters from a string.

    Args:
        sentence (str): the string you want to fix

    Returns:
        (str): the string without non english characters
    """
    return re.sub(r"[^\u0000-\u05C0\u2100-\u214F]+", "", sentence)


def clean_html_text(input_text: str):
    """Clean a text removing html taggings and informations to keep only a clean simple text.

    Args:
        input_text (str): the text to clean

    Returns:
        (str): the cleaned text
    """
    output_text = html.unescape(input_text)
    output_text = output_text.replace("<br>", " ")
    output_text = " ".join(BeautifulSoup(re.sub(r"http\S+", "", output_text, flags=re.MULTILINE), "lxml").text.split())

    return remove_non_en_chars(output_text)


def pandas_html_text_cleaner(column: pd.Series) -> pd.Series:
    """Clean a text in a pandas dataframe removing html taggings and informations to keep only a clean simple text.

    Args:
        column (pd.Series): the text column to clean with html tags

    Returns:
        (pd.Series): the cleaned text column without html tags

    """
    return column.apply(
        lambda x: " ".join(BeautifulSoup(re.sub(r"http\S+", "", x, flags=re.MULTILINE), "lxml").text.split())
    )


def serialize_numpy(numpy: np.ndarray) -> bytes:
    """Serialize numpy array into bytestring.

    Source: https://stackoverflow.com/a/30699208

    Args:
        numpy (dict): Numpy array to serialize

    Returns:
        bytes: Serialized array
    """
    mem_file = io.BytesIO()
    np.save(mem_file, numpy)

    return mem_file.getvalue()


def deserialize_numpy(serialized_array: bytes) -> np.ndarray:
    """Deserialize bytestring into numpy array.

    Source: https://stackoverflow.com/a/30699208

    Args:
        serialized_array (bytes): Serialized array

    Returns:
        np.ndarray: Deserialized numpy array
    """
    mem_file = io.BytesIO()

    # Deserializing bytestring
    mem_file.write(serialized_array)
    mem_file.seek(0)

    return np.load(mem_file)


def hash_object(obj: Union[str, dict], hash_algorithm: str = "sha256") -> str:
    """Returns a unique string given the `obj` values using an hash algorithm.

    Args:
        obj (Union[str, dict]): Input object. Must be a `str` or `dict`
        hash_algorithm (str, optional): Hash algorithm to use.
            Options: `"md5"`, `"sha1"` or `"sha256"`
            Defaults to "sha256".

    Raises:
        ValueError: In case `obj` or `hash_algorithm` are invalid types

    Returns:
        str: Hashed object
    """
    hash_algorithms = {
        "md5": hashlib.md5(usedforsecurity=False),
        "sha1": hashlib.sha1(usedforsecurity=False),
        "sha256": hashlib.sha256(),
    }
    if hash_algorithm not in hash_algorithms.keys():
        e = f"Invalid `hash_algorithm` ({hash_algorithm}); Must be one of: {hash_algorithms}"
        logger.error(e)
        raise ValueError(e)

    if isinstance(obj, str):
        encoded_obj = obj.encode(encoding="utf-8")
    elif isinstance(obj, dict):
        obj = dict(FlatDict(obj, delimiter="."))
        encoded_obj = json.dumps(obj, sort_keys=True).encode(encoding="utf-8")
    else:
        raise ValueError(f"`obj` type ({type(obj)}) non-supported; cannot hash object")

    hash_obj = hash_algorithms[hash_algorithm]
    hash_obj.update(encoded_obj)
    return hash_obj.hexdigest()
