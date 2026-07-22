"""
AlphaLens Benchmark Return Extraction

Extracts benchmark returns from a normalized dataset.
"""

from __future__ import annotations

import pandas as pd

from app.io.normalizer import CANONICAL_BENCHMARK


def extract_benchmark_returns(
    df: pd.DataFrame,
) -> pd.Series | None:
    """
    Extract benchmark percentage returns.

    Parameters
    ----------
    df : pd.DataFrame
        Normalized DataFrame.

    Returns
    -------
    pd.Series | None
        Benchmark return series, or None if the dataset has no benchmark.
    """

    if CANONICAL_BENCHMARK not in df.columns:
        return None

    returns = (
        df[CANONICAL_BENCHMARK]
        .pct_change()
        .dropna()
    )

    returns.name = "Benchmark Returns"

    return returns