"""
AlphaLens Schema Detector

Detects which columns represent the date, portfolio value,
and benchmark value without modifying the dataset.
"""

from __future__ import annotations

import re

import pandas as pd

from dataclasses import dataclass


DATE_ALIASES = {
    "date",
    "trade date",
    "datetime",
    "timestamp",
    "time",
}

PORTFOLIO_ALIASES = {
    "portfolio",
    "portfolio value",
    "portfolio nav",
    "nav",
    "equity",
    "equity curve",
    "strategy value",
    "strategy equity",
    "account value",
    "total value",
}

BENCHMARK_ALIASES = {
    "benchmark",
    "benchmark value",
    "index",
    "market",
    "spy",
    "nifty50",
    "nifty 50",
}

@dataclass(frozen=True)
class SchemaMapping:
    """
    Mapping between the dataset's original columns and AlphaLens'
    canonical schema.
    """

    date: str
    portfolio: str
    benchmark: str | None = None


def _normalize_column_name(name: str) -> str:
    """
    Normalize a column name for robust matching.

    Examples
    --------
    Trade_Date   -> trade date
    TRADE-DATE   -> trade date
    Portfolio    -> portfolio
    """

    name = name.strip().lower()

    name = re.sub(r"[^a-z0-9]+", " ", name)

    name = re.sub(r"\s+", " ", name).strip()

    return name


def _find_column(
    columns: pd.Index,
    aliases: set[str],
) -> str | None:
    """
    Find the first column whose normalized name matches one of the aliases.

    Parameters
    ----------
    columns : pd.Index
        DataFrame column names.

    aliases : set[str]
        Accepted normalized aliases.

    Returns
    -------
    str | None
        Original column name if found, otherwise None.
    """

    for column in columns:
        normalized = _normalize_column_name(str(column))

        if normalized in aliases:
            return str(column)

    return None

def detect_schema(df: pd.DataFrame) -> SchemaMapping:
    """
    Detect the schema of a portfolio dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Validated input DataFrame.

    Returns
    -------
    SchemaMapping
        Mapping from the dataset's original columns to the AlphaLens
        canonical schema.

    Raises
    ------
    ValueError
        If required columns cannot be identified.
    """

    date_column = _find_column(df.columns, DATE_ALIASES)
    portfolio_column = _find_column(df.columns, PORTFOLIO_ALIASES)
    benchmark_column = _find_column(df.columns, BENCHMARK_ALIASES)

    if date_column is None:
        raise ValueError(
            "Unable to detect a date column. "
            "Please ensure your dataset contains a date field."
        )

    if portfolio_column is None:
        raise ValueError(
            "Unable to detect a portfolio value column. "
            "Please ensure your dataset contains a portfolio, NAV, or equity column."
        )

    return SchemaMapping(
        date=date_column,
        portfolio=portfolio_column,
        benchmark=benchmark_column,
    )