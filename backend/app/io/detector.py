"""
AlphaLens Dataset Detector
"""

from __future__ import annotations

import pandas as pd


SUPPORTED_SCHEMAS = {
    "returns": ["Returns"],
    "portfolio": ["Portfolio Value"],
    "prices": ["Close"],
}


def detect_dataset_type(df: pd.DataFrame) -> str:
    """
    Detect the type of dataset from its columns.
    """

    columns = set(df.columns)

    for dataset_type, required_columns in SUPPORTED_SCHEMAS.items():

        if all(column in columns for column in required_columns):
            return dataset_type

    raise ValueError(
        f"Unsupported dataset.\nFound columns: {list(df.columns)}"
    )