"""
AlphaLens Data Normalizer

Converts a detected dataset into AlphaLens' canonical schema.
"""

from __future__ import annotations

import pandas as pd

from .detector import SchemaMapping


CANONICAL_DATE = "Date"
CANONICAL_PORTFOLIO = "Portfolio Value"
CANONICAL_BENCHMARK = "Benchmark Value"


def normalize_dataframe(
    df: pd.DataFrame,
    schema: SchemaMapping,
) -> pd.DataFrame:
    """
    Normalize a validated dataset into AlphaLens' canonical schema.

    Parameters
    ----------
    df : pd.DataFrame
        Original validated DataFrame.

    schema : SchemaMapping
        Mapping detected by detector.py.

    Returns
    -------
    pd.DataFrame
        Normalized DataFrame.
    """

    normalized = df.copy()

    rename_map = {
        schema.date: CANONICAL_DATE,
        schema.portfolio: CANONICAL_PORTFOLIO,
    }

    if schema.benchmark is not None:
        rename_map[schema.benchmark] = CANONICAL_BENCHMARK

    normalized = normalized.rename(columns=rename_map)

    normalized[CANONICAL_DATE] = pd.to_datetime(
        normalized[CANONICAL_DATE],
        errors="raise",
    )

    normalized = normalized.sort_values(CANONICAL_DATE)

    normalized = normalized.set_index(CANONICAL_DATE)

    return normalized