"""
AlphaLens Frequency Detection

Detects the sampling frequency of a normalized dataset.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd



@dataclass(frozen=True)
class FrequencyInfo:
    """
    Information about detected dataset frequency.
    """

    name: str

    annualization_factor: int

    pandas_frequency: str | None = None



def detect_frequency(
    df: pd.DataFrame,
) -> FrequencyInfo:
    """
    Detect dataset frequency.

    Uses median date spacing instead of
    pandas infer_freq because financial datasets
    contain missing weekends and holidays.
    """

    if not isinstance(
        df.index,
        pd.DatetimeIndex,
    ):

        raise TypeError(
            "Frequency detection requires a DatetimeIndex."
        )


    if len(df.index) < 2:

        return FrequencyInfo(
            name="Unknown",
            annualization_factor=252,
            pandas_frequency=None,
        )



    dates = (
        df.index
        .sort_values()
    )


    deltas = (
        dates
        .to_series()
        .diff()
        .dropna()
    )


    median_days = (
        deltas
        .median()
        .days
    )



    # -------------------------
    # Financial frequency rules
    # -------------------------


    if median_days <= 1:

        return FrequencyInfo(
            name="Daily",
            annualization_factor=252,
            pandas_frequency="D",
        )


    elif median_days <= 7:

        return FrequencyInfo(
            name="Weekly",
            annualization_factor=52,
            pandas_frequency="W",
        )


    elif median_days <= 31:

        return FrequencyInfo(
            name="Monthly",
            annualization_factor=12,
            pandas_frequency="ME",
        )


    elif median_days <= 100:

        return FrequencyInfo(
            name="Quarterly",
            annualization_factor=4,
            pandas_frequency="QE",
        )


    else:

        return FrequencyInfo(
            name="Yearly",
            annualization_factor=1,
            pandas_frequency="YE",
        )