"""
AlphaLens Rolling Analytics
"""

from __future__ import annotations

import pandas as pd

from app.analytics.returns import validate_returns
from app.analytics.performance import sharpe_ratio
from app.analytics.returns import volatility
from app.analytics.drawdown import drawdown_series


def rolling_sharpe(
    returns: pd.Series,
    window: int = 63,
) -> pd.Series:
    """
    Rolling annualized Sharpe Ratio.
    """

    returns = validate_returns(returns)

    return returns.rolling(window).apply(
        lambda x: sharpe_ratio(pd.Series(x)),
        raw=False,
    )


def rolling_volatility(
    returns: pd.Series,
    window: int = 63,
) -> pd.Series:
    """
    Rolling annualized volatility.
    """

    returns = validate_returns(returns)

    return returns.rolling(window).apply(
        lambda x: volatility(pd.Series(x)),
        raw=False,
    )


def rolling_drawdown(
    returns: pd.Series,
) -> pd.Series:
    """
    Drawdown through time.
    """

    returns = validate_returns(returns)

    return drawdown_series(returns)