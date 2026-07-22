"""
AlphaLens Return Extraction

Converts a normalized portfolio value series into periodic returns.
"""

from __future__ import annotations

import pandas as pd

from app.io.normalizer import CANONICAL_PORTFOLIO


def extract_returns(df: pd.DataFrame) -> pd.Series:
    """
    Extract portfolio percentage returns.

    Parameters
    ----------
    df : pd.DataFrame
        Normalized DataFrame.

    Returns
    -------
    pd.Series
        Portfolio return series.
    """

    returns = (
        df[CANONICAL_PORTFOLIO]
        .pct_change()
        .dropna()
    )

    returns.name = "Portfolio Returns"

    return returns