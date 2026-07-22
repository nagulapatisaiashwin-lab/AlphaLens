"""
AlphaLens Performance Analytics
"""

from __future__ import annotations

import pandas as pd

from app.analytics.returns import (
    annualized_return,
    volatility,
)


def sharpe_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.0,
    periods_per_year: int = 252,
) -> float:
    """
    Compute annualized Sharpe Ratio.
    """

    ann_return = annualized_return(
        returns,
        periods_per_year=periods_per_year,
    )

    ann_vol = volatility(
        returns,
        periods_per_year=periods_per_year,
    )

    if ann_vol == 0:
        return 0.0

    return (ann_return - risk_free_rate) / ann_vol