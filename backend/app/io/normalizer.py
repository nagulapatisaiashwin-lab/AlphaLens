"""
AlphaLens Dataset Normalizer
"""

from __future__ import annotations

import pandas as pd

from app.io.detector import detect_dataset_type


def extract_returns(df: pd.DataFrame) -> pd.Series:
    """
    Convert supported datasets into a standardized
    return series.
    """

    dataset_type = detect_dataset_type(df)

    if dataset_type == "returns":
        return df["Returns"]

    if dataset_type == "portfolio":
        return df["Portfolio Value"].pct_change().dropna()

    if dataset_type == "prices":
        return df["Close"].pct_change().dropna()

    raise ValueError("Unsupported dataset.")