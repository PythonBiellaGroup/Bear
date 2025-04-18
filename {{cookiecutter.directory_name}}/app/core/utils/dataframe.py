import json

import pandas as pd
import yaml
from loguru import logger
from pandas import DataFrame

from app.core.utils.files import search_path


def remove_dict_none_values(dictionary: dict) -> list:
    """Remove dictionary keys whose value is None.

    Args:
        dictionary [dict]: dictionary to clean

    Returns:
        a list of keys without none values
    """
    return list(map(dictionary.pop, [i for i in dictionary if dictionary[i] is None]))


def data_iterator(data: pd.DataFrame, batch_size: int):
    """Yield batches of the input dataframe with a sequential index.

    Args:
        data (pd.DataFrame): input dataframe
        batch_size (int): size of the batch
    """
    for i in range(0, len(data), batch_size):
        yield data.iloc[i : i + batch_size]


def semi_join(left: DataFrame, right: DataFrame, left_on: str, right_on: str) -> DataFrame:
    """Pandas dataframe semi join.

    Args:
        left (DataFrame): left dataframe
        right (DataFrame): right dataframe
        left_on (str): column name of the left dataframe
        right_on (str): column name of the right dataframe

    Returns:
        Pandas DataFrame: the left dataframe with only the rows that are in the right dataframe
    """
    semi = right[right_on].drop_duplicates() if not right.empty else []
    is_in = left[left_on].isin(semi)
    return left[is_in]


def semi_join_if_any(left: DataFrame, right: DataFrame, left_on: str, right_on: str) -> DataFrame:
    """Pandas dataframe semi join.

    Args:
        left (DataFrame): left dataframe
        right (DataFrame): right dataframe
        left_on (str): column name of the left dataframe
        right_on (str): column name of the right dataframe

    Returns:
        Pandas DataFrame: the left dataframe with only the rows that are in the right dataframe
    """
    if right.empty:
        return left

    return semi_join(left, right, left_on, right_on)


def anti_join(left: DataFrame, right: DataFrame, left_on: str, right_on: str) -> DataFrame:
    """Pandas dataframe anti join.

    Args:
        left (DataFrame): left dataframe
        right (DataFrame): right dataframe
        left_on (str): column name of the left dataframe
        right_on (str): column name of the right dataframe

    Returns:
        Pandas DataFrame: the left dataframe with only the rows that are not in the right dataframe
    """
    semi = right[right_on].drop_duplicates()
    is_in = left[left_on].isin(semi)
    return left[~is_in]


def remove_columns(dataset: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Remove columns from a pandas dataframe.

    Args:
        dataset (pd.DataFrame): pandas dataframe as input
        cols (list of strings): list of columns you want to remove

    Returns:
        the dataset without the columns
    """
    if isinstance(cols, str):
        cols = [cols]
    cols = [c for c in cols if c in dataset.columns]
    return dataset.drop(cols, axis=1)


def keep_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Keep only the columns you want in a pandas dataframe and remove everything else.

    Args:
        df (pd.DataFrame): input pandas dataframe
        cols (list): the list of columns you want to keep inside the pandas dataframe

    Returns:
        (pd.DataFrame): the dataframe with only the columns you want to keep
    """
    if isinstance(cols, str):
        cols = [cols]
    cols = [c for c in cols if c in df.columns]
    return df.loc[:, cols]


def save_dict_to_json(d: dict, file: str) -> str:
    """Save a dictionary to a json file.

    Args:
        d (dict): the dictionary to save
        file (str): the file path or filename where you want to save the dictionary

    Returns:
        (str): the filepath of the saved file
    """
    with open(file, "w") as fp:
        json.dump(d, fp, sort_keys=True, indent=4)
    return file


# Check Dataframe Utility function
def check_df(dataframe: pd.DataFrame, sample: bool = False) -> None:  # noqa
    """Get the informations about a pandas dataframe (shape, columns, dtypes, ...).

    This function use the logger to print the informations (with an "info" level)

    Args:
        dataframe (pd.DataFrame): the pandas dataframe you want to check
        sample (bool): If you want also a sample of top 5 rows. Defaults to False.
    """
    logger.info(f"Dataframe Shape: {dataframe.shape} with rows: {dataframe.shape[0]} and columns: {dataframe.shape[1]}")
    logger.info(f"\nDF Columns: \n{list(dataframe.columns)}")
    if sample:
        logger.info(f"\nData:\n{dataframe.head(5)}")


def write_dataset_yaml(to_path: str = "", filename: str = "", dataset: pd.DataFrame = None) -> bool:
    """Write a pandas dataset to yaml.

    Args:
        to_path (str, optional): Path where you want to save the yaml file. Defaults to "".
        filename (str, optional): Name of the file to use. Defaults to "".
        dataset (pd.DataFrame, optional): Pandas dataframe to save. Defaults to None.

    Returns:
        bool: If the
    """
    file_path = search_path(to_path, filename)

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
