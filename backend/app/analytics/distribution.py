"""
AlphaLens Distribution Analytics
"""

from __future__ import annotations

import pandas as pd

from app.analytics.returns import validate_returns


def standard_deviation(returns: pd.Series) -> float:
    """Standard deviation of returns."""
    returns = validate_returns(returns)
    return float(returns.std())


def skewness(returns: pd.Series) -> float:
    """Sample skewness."""
    returns = validate_returns(returns)
    return float(returns.skew())


def kurtosis(returns: pd.Series) -> float:
    """Sample kurtosis."""
    returns = validate_returns(returns)
    return float(returns.kurt())


def percentile(returns: pd.Series, q: float) -> float:
    """
    Compute percentile.

    q should be between 0 and 100.
    """
    returns = validate_returns(returns)
    return float(returns.quantile(q / 100))


def interquartile_range(returns: pd.Series) -> float:
    """Compute IQR."""
    returns = validate_returns(returns)
    q75 = returns.quantile(0.75)
    q25 = returns.quantile(0.25)
    return float(q75 - q25)