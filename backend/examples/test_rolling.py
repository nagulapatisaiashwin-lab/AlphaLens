"""
Test script for AlphaLens Rolling Analytics
"""

import sys
from pathlib import Path

# Add backend directory to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.io.loader import load_csv
from app.io.normalizer import extract_returns

from app.analytics.rolling import (
    rolling_sharpe,
    rolling_volatility,
    rolling_drawdown,
)


def main() -> None:
    # Load sample dataset
    df = load_csv("examples/sample_returns.csv")

    # Extract standardized returns
    returns = extract_returns(df)

    print("=" * 60)
    print("Rolling Sharpe")
    print("=" * 60)
    print(rolling_sharpe(returns, window=3))

    print("\n" + "=" * 60)
    print("Rolling Volatility")
    print("=" * 60)
    print(rolling_volatility(returns, window=3))

    print("\n" + "=" * 60)
    print("Rolling Drawdown")
    print("=" * 60)
    print(rolling_drawdown(returns))


if __name__ == "__main__":
    main()