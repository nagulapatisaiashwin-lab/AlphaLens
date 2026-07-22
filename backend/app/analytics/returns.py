"""
AlphaLens Returns Analytics

Core functions for computing simple and cumulative returns.
"""

from __future__ import annotations

import pandas as pd


def validate_returns(returns: pd.Series) -> pd.Series:
    """
    Validate a return series.

    Parameters
    ----------
    returns : pd.Series
        Series of periodic returns.

    Returns
    -------
    pd.Series
        Cleaned return series.
    """

    if not isinstance(returns, pd.Series):
        raise TypeError("returns must be a pandas Series")

    returns = returns.dropna()

    if returns.empty:
        raise ValueError("return series is empty")

    return returns.astype(float)


def cumulative_returns(returns: pd.Series) -> pd.Series:
    """
    Compute cumulative returns.

    Formula:
        (1+r1)(1+r2)...(1+rn)-1
    """

    returns = validate_returns(returns)

    return (1 + returns).cumprod() - 1

def total_return(returns: pd.Series) -> float:
    """
    Compute total return.

    Formula:
        Π(1+r) - 1
    """

    returns = validate_returns(returns)

    return float((1 + returns).prod() - 1)


def annualized_return(
    returns: pd.Series,
    periods_per_year: int = 252,
) -> float:
    """
    Compute annualized return (CAGR).

    Formula:
        (Ending Value)^(periods_per_year / n) - 1
    """

    returns = validate_returns(returns)

    cumulative = (1 + returns).prod()
    n = len(returns)

    return float(cumulative ** (periods_per_year / n) - 1)


def volatility(
    returns: pd.Series,
    periods_per_year: int = 252,
) -> float:
    """
    Compute annualized volatility.
    """

    returns = validate_returns(returns)

    return float(returns.std() * (periods_per_year ** 0.5))