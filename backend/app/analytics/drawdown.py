"""
AlphaLens Drawdown Analytics
"""

from __future__ import annotations

import pandas as pd

from app.analytics.returns import cumulative_returns


def drawdown_series(returns: pd.Series) -> pd.Series:
    """
    Compute the drawdown series from periodic returns.
    """

    equity = (1 + cumulative_returns(returns))
    running_max = equity.cummax()

    return (equity - running_max) / running_max


def max_drawdown(returns: pd.Series) -> float:
    """
    Compute the maximum drawdown.
    """

    return float(drawdown_series(returns).min())