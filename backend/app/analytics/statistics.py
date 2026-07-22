"""
AlphaLens Statistics Analytics
"""

from __future__ import annotations

import pandas as pd

from app.analytics.returns import validate_returns


def mean_return(returns: pd.Series) -> float:
    returns = validate_returns(returns)
    return float(returns.mean())


def median_return(returns: pd.Series) -> float:
    returns = validate_returns(returns)
    return float(returns.median())


def best_day(returns: pd.Series) -> float:
    returns = validate_returns(returns)
    return float(returns.max())


def worst_day(returns: pd.Series) -> float:
    returns = validate_returns(returns)
    return float(returns.min())


def positive_days(returns: pd.Series) -> int:
    returns = validate_returns(returns)
    return int((returns > 0).sum())


def negative_days(returns: pd.Series) -> int:
    returns = validate_returns(returns)
    return int((returns < 0).sum())


def win_rate(returns: pd.Series) -> float:
    returns = validate_returns(returns)
    return float((returns > 0).mean())