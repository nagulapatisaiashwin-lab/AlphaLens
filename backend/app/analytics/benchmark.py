"""
AlphaLens Benchmark Analytics
"""

from __future__ import annotations

import pandas as pd

from app.analytics.returns import (
    validate_returns,
    annualized_return,
)


def _align_returns(
    portfolio: pd.Series,
    benchmark: pd.Series,
) -> tuple[pd.Series, pd.Series]:
    """
    Validate and align portfolio and benchmark returns.
    """

    portfolio = validate_returns(portfolio)
    benchmark = validate_returns(benchmark)

    portfolio, benchmark = portfolio.align(
        benchmark,
        join="inner",
    )

    if portfolio.empty:
        raise ValueError(
            "Portfolio and benchmark have no overlapping observations."
        )

    return portfolio, benchmark


def correlation(
    portfolio: pd.Series,
    benchmark: pd.Series,
) -> float:
    """
    Correlation between portfolio and benchmark returns.
    """

    portfolio, benchmark = _align_returns(
        portfolio,
        benchmark,
    )

    return float(portfolio.corr(benchmark))


def beta(
    portfolio: pd.Series,
    benchmark: pd.Series,
) -> float:
    """
    Portfolio beta relative to the benchmark.

    β = Cov(Rp, Rb) / Var(Rb)
    """

    portfolio, benchmark = _align_returns(
        portfolio,
        benchmark,
    )

    variance = benchmark.var()

    if variance == 0:
        return 0.0

    covariance = portfolio.cov(benchmark)

    return float(covariance / variance)


def alpha(
    portfolio: pd.Series,
    benchmark: pd.Series,
    risk_free_rate: float = 0.0,
    periods_per_year: int = 252,
) -> float:
    """
    Jensen's Alpha.
    """

    portfolio, benchmark = _align_returns(
        portfolio,
        benchmark,
    )

    portfolio_return = annualized_return(
        portfolio,
        periods_per_year=periods_per_year,
    )

    benchmark_return = annualized_return(
        benchmark,
        periods_per_year=periods_per_year,
    )

    b = beta(
        portfolio,
        benchmark,
    )

    return float(
        portfolio_return
        - (
            risk_free_rate
            + b * (benchmark_return - risk_free_rate)
        )
    )


def tracking_error(
    portfolio: pd.Series,
    benchmark: pd.Series,
    periods_per_year: int = 252,
) -> float:
    """
    Annualized tracking error.
    """

    portfolio, benchmark = _align_returns(
        portfolio,
        benchmark,
    )

    active_returns = portfolio - benchmark

    return float(
        active_returns.std()
        * (periods_per_year ** 0.5)
    )


def active_return(
    portfolio: pd.Series,
    benchmark: pd.Series,
    periods_per_year: int = 252,
) -> float:
    """
    Annualized active return.
    """

    portfolio, benchmark = _align_returns(
        portfolio,
        benchmark,
    )

    return float(
        annualized_return(
            portfolio,
            periods_per_year=periods_per_year,
        )
        - annualized_return(
            benchmark,
            periods_per_year=periods_per_year,
        )
    )


def information_ratio(
    portfolio: pd.Series,
    benchmark: pd.Series,
    periods_per_year: int = 252,
) -> float:
    """
    Information Ratio.
    """

    te = tracking_error(
        portfolio,
        benchmark,
        periods_per_year=periods_per_year,
    )

    if te == 0:
        return 0.0

    ar = active_return(
        portfolio,
        benchmark,
        periods_per_year=periods_per_year,
    )

    return float(ar / te)