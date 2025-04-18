import datetime as dt
from datetime import date, datetime, timedelta, timezone
from typing import Any, Optional

import numpy as np
import pandas as pd

from app.core.utils.conversions import date2millis, millis2date

# from typing import Any, Callable, TypeVar
# SF = TypeVar("SF", bound=Callable[..., Any])
# VF = TypeVar("VF", bound=Callable[..., np.array])
# vectorize: Callable[[SF], VF] = np.vectorize

# Current date (with a format)
# Current week number
# Current time


@np.vectorize
def datetime_now():
    """Get the current date and time."""
    return datetime.now(timezone.utc)


@np.vectorize
def date_now_plus_30_days():
    """Get the current date plus 30 days."""
    return datetime.now(timezone.utc) + timedelta(days=30)


@np.vectorize
def datetime_now_plus_7_days():
    """Get the current date plus 7 days."""
    return datetime.now(timezone.utc) + timedelta(days=7)


@np.vectorize
def datetime_now_plus_1_year():
    """Get the current date plus 1 year."""
    return datetime.now(timezone.utc) + timedelta(days=365)


@np.vectorize
def first_day_of_month(any_day: date) -> date:
    """Get the first day of the month for any day.

    Args:
        any_day (date): Any day

    Returns:
        date: First day of the month
    """
    return any_day.replace(day=1)


@np.vectorize
def last_day_of_month(any_day: date) -> date:
    """Get the last day of the month for any day.

    Args:
        any_day (date): Any day

    Returns:
        date: Last day of the month

    """
    # this will never fail
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = any_day.replace(day=28) + timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - timedelta(days=next_month.day)


@np.vectorize
def last_day_of_week(date: date) -> date:
    """Get the last day of the week for any day.

    Args:
        date (date): Any day

    Returns:
        date: Last day of the week

    """
    start = date - timedelta(days=date.weekday())
    return start + timedelta(days=6)


# milliseconds
@np.vectorize
def ms_to_date(ms: int) -> np.array:
    """Convert milliseconds to date (datetime).

    Warning: the results it's a numpy array

    Args:
        ms (int): Milliseconds to convert
    Returns:
        np.array(dt.datetime): Converted date
    """
    return millis2date(ms)


@np.vectorize
def date_to_ms(x: str, date_format: str = "%Y-%m-%d %H:%M:%S") -> np.array:
    """Convert a date in a string format to milliseconds using a specific format.

    Warning: the results it's a numpy array

    Args:
        x (str): Date to convert
        format_date (str, optional): Format of the date. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        np.array(dt.datime): Converted date
    """
    return date2millis(x, date_format)


# Strings
@np.vectorize
def str_to_date(x: str, date_format: str = "%Y-%m-%d") -> dt.date:
    """Convert a string to date.

    Args:
        x: String to convert
        format (str, optional): Format of the string. Defaults to "%Y-%m-%d".

    Returns:
        dt.date: Converted date
    """
    return dt.datetime.strptime(x, date_format).replace(tzinfo=dt.timezone.utc).date()


@np.vectorize
def date_to_str(x: date, date_format: str = "%Y-%m-%d") -> str:
    """Date to string.

    Args:
        x (date): Date to convert
        format (str): Format of the string. Defaults to "%Y-%m-%d".

    Returns:
        str: Converted string
    """
    return x.strftime(date_format) if not pd.isnull(x) else np.nan


@np.vectorize
def str_to_datetime(x: str, date_format: str = "%Y-%m-%d %H:%M:%S") -> dt.datetime:
    """String to datetime.

    Args:
        x (str): String to convert
        format (str): Format of the string. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        dt.datetime: Converted datetime
    """
    return dt.datetime.strptime(x, date_format).replace(tzinfo=dt.timezone.utc)


@np.vectorize
def datetime_to_str(x: date, date_format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Convert Datetime to string.

    Args:
        x (date): Datetime to convert
        format (str): Format of the string. Defaults to "%Y-%m-%d %H:%M:%S".

    Return:
        str: Converted string

    """
    return x.strftime(date_format) if not pd.isnull(x) else np.nan


# generic
@np.vectorize
def acquire_date(x: Optional[Any], date_format: str = "%Y-%m-%d %H:%M:%S") -> Any:
    """Acquire and output a date from a string.

    Args:
        x (Optional[Any]): String to convert
        format (str): Format of the string. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        Any: Extracted date
    """
    if isinstance(x, str):
        return (
            dt.datetime.strptime(x, date_format).replace(tzinfo=dt.timezone.utc).date() if not pd.isnull(x) else np.nan
        )

    if isinstance(x, dt.date):
        return x

    return np.nan


def is_timezone_aware(dt):
    """Check if a datetime object is timezone aware.

    Args:
        dt (datetime): The datetime object to check.

    Returns:
        bool: True if the datetime object is timezone aware, False otherwise.
    """
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None
