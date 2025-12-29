"""
data_loader.py
Handles loading and validation of CSV datasets.
"""

import pandas as pd


class DataLoadError(Exception):
    """Custom exception for dataset loading errors."""


def load_csv(filepath, expected_columns):
    """
    Load a CSV file and validate required columns.

    Parameters:
        filepath (str): Path to CSV file
        expected_columns (list): Required column names

    Returns:
        pandas.DataFrame
    """
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        raise DataLoadError(f"Failed to load {filepath}: {e}") from e

    missing = set(expected_columns) - set(df.columns)
    if missing:
        raise DataLoadError(f"Missing columns {missing} in {filepath}")

    return df
