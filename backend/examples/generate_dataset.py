"""
Generate a realistic dataset for AlphaLens.

Creates approximately five years of business-day data
containing a portfolio and benchmark equity curve.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


TRADING_DAYS = 252
YEARS = 5
INITIAL_CAPITAL = 100_000


def generate_equity_curve(
    annual_return: float,
    annual_volatility: float,
    initial_value: float,
    periods: int,
) -> pd.Series:
    """
    Generate a geometric random walk equity curve.
    """

    daily_return = annual_return / TRADING_DAYS
    daily_vol = annual_volatility / np.sqrt(TRADING_DAYS)

    returns = np.random.normal(
        loc=daily_return,
        scale=daily_vol,
        size=periods,
    )

    equity = initial_value * np.cumprod(1 + returns)

    return pd.Series(equity)


def main():

    np.random.seed(42)

    periods = YEARS * TRADING_DAYS

    dates = pd.bdate_range(
        start="2020-01-01",
        periods=periods,
    )

    portfolio = generate_equity_curve(
        annual_return=0.16,
        annual_volatility=0.18,
        initial_value=INITIAL_CAPITAL,
        periods=periods,
    )

    benchmark = generate_equity_curve(
        annual_return=0.11,
        annual_volatility=0.15,
        initial_value=INITIAL_CAPITAL,
        periods=periods,
    )

    df = pd.DataFrame(
        {
            "Date": dates,
            "Portfolio Value": portfolio,
            "Benchmark Value": benchmark,
        }
    )

    df.to_csv(
        "examples/realistic_returns.csv",
        index=False,
    )

    print("Dataset generated successfully!")
    print(df.head())
    print()
    print(f"Rows : {len(df)}")
    print("Saved to examples/realistic_returns.csv")


if __name__ == "__main__":
    main()