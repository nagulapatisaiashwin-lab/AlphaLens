"""
Generate rolling analytics charts.
"""

import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.analytics.rolling import rolling_sharpe
from app.io.loader import load_csv
from app.io.normalizer import extract_returns
from app.visualization.rolling import plot_rolling_metric


def main():

    df = load_csv("examples/realistic_returns.csv")

    returns = extract_returns(df)

    window = 126

    sharpe = rolling_sharpe(returns, window)

    plot_rolling_metric(
        sharpe,
        df["Date"].iloc[1:],
        "Rolling Sharpe Ratio",
        "Sharpe",
        "rolling_sharpe.html",
    )


if __name__ == "__main__":
    main()