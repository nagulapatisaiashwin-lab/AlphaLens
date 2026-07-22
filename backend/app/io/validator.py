"""
AlphaLens Data Validator

Validates the structural integrity of a loaded dataset before schema
detection and normalization.
"""

from __future__ import annotations

import pandas as pd


def validate_dataframe(df: pd.DataFrame) -> None:
    """
    Validate the structure of a loaded DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Raw DataFrame returned by the loader.

    Raises
    ------
    ValueError
        If the DataFrame fails any structural validation checks.
    """

    if df.empty:
        raise ValueError("The dataset is empty.")

    if len(df.columns) == 0:
        raise ValueError("The dataset contains no columns.")

    if df.columns.has_duplicates:
        duplicates = df.columns[df.columns.duplicated()].tolist()
        raise ValueError(
            f"Duplicate column names found: {duplicates}"
        )

    invalid_columns = [
        column
        for column in df.columns
        if pd.isna(column) or str(column).strip() == ""
    ]

    if invalid_columns:
        raise ValueError(
            "The dataset contains blank column names."
        )

    if len(df) == 0:
        raise ValueError("The dataset contains no rows.")