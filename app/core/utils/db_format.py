from decimal import Decimal
from typing import Optional, Union

import numpy as np


def format_db_month(date: str) -> str:
    """Format month string into Postgres date field.

    Args:
        date (str): Date string

    Returns:
        str: Postgres formatted date
    """
    if str(date) == "nan":
        return "NULL"
    return f"TO_DATE('{date}','YYYY-MM')"


def format_db_week(date: str) -> str:
    """Format week string into Postgres date field.

    Args:
        date (str): Date string

    Returns:
        str: Postgres formatted date
    """
    if str(date) == "nan":
        return "NULL"
    return f"TO_DATE('{date}','YYYY-wIW')"


def format_db_date(date: str) -> str:
    """Format date string into Postgres date field.

    Args:
        date (str): Date string

    Returns:
        str: Postgres formatted date
    """
    if str(date) == "nan":
        return "NULL"
    return f"TO_DATE('{date}','YYYY-MM-DD')"


def format_db_string(x: Optional[str]) -> str:
    """Format a string and replace quotes for postgres compatibility.

    Args:
        x (str): String to format

    Returns:
        str: Postgres formatted string
    """
    if x is not None:
        x = x.replace("'", "''")
        x = x.replace(":", ": ")

    return f"'{x}'"


def format_db_float(x: Union[float, Decimal, str]) -> float:
    """Format float or decimal types for postgres compatibility.

    Args:
        x (Union[float, Decimal]): Float to format

    Returns:
        float: Postgres formatted float
    """
    if x is None or x == "":
        return 0
    if np.isnan(float(x)):
        return 0

    return float(x)


def format_db_int(x: Union[int, float, str]) -> int:
    """Format integer or float in integer.

    Args:
        x (Union[int, float]): Integer or float to format

    Returns:
        int: Postgres formatted integer
    """
    if x is None or x == "":
        return 0
    if np.isnan(float(x)):
        return 0

    x = float(x)
    return int(x)
