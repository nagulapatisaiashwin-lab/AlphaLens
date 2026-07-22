"""
AlphaLens Risk Analytics
"""

from __future__ import annotations

import pandas as pd

from app.analytics.returns import (
    validate_returns,
    annualized_return,
)

from app.analytics.drawdown import max_drawdown


DEFAULT_PERIODS_PER_YEAR = 252


def downside_deviation(
    returns: pd.Series,
    periods_per_year: int = DEFAULT_PERIODS_PER_YEAR,
) -> float:
    """
    Annualized downside deviation.
    """

    returns = validate_returns(returns)

    downside = returns[returns < 0]

    if len(downside) == 0:
        return 0.0

    return float(downside.std() * (periods_per_year ** 0.5))


def sortino_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.0,
    periods_per_year: int = DEFAULT_PERIODS_PER_YEAR,
) -> float:
    """
    Annualized Sortino Ratio.
    """

    returns = validate_returns(returns)

    downside = downside_deviation(
        returns,
        periods_per_year=periods_per_year,
    )

    if downside == 0:
        return 0.0

    excess_return = annualized_return(
        returns,
        periods_per_year=periods_per_year,
    ) - risk_free_rate

    return float(excess_return / downside)


def calmar_ratio(
    returns: pd.Series,
    periods_per_year: int = DEFAULT_PERIODS_PER_YEAR,
) -> float:
    """
    Calmar Ratio.
    """

    cagr = annualized_return(
        returns,
        periods_per_year=periods_per_year,
    )

    mdd = abs(max_drawdown(returns))

    if mdd == 0:
        return 0.0

    return float(cagr / mdd)


def value_at_risk(
    returns: pd.Series,
    confidence: float = 0.95,
) -> float:
    """
    Historical Value at Risk.
    """

    returns = validate_returns(returns)

    return float(returns.quantile(1 - confidence))


def conditional_value_at_risk(
    returns: pd.Series,
    confidence: float = 0.95,
) -> float:
    """
    Historical Expected Shortfall.
    """

    returns = validate_returns(returns)

    var = value_at_risk(returns, confidence)

    losses = returns[returns <= var]

    if len(losses) == 0:
        return var

    return float(losses.mean())