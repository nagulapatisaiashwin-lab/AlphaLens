"""
Generate AlphaLens Equity Curve
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.io.loader import load_csv
from app.visualization.equity import plot_equity_curve


def main():

    df = load_csv("examples/realistic_returns.csv")

    plot_equity_curve(df)


if __name__ == "__main__":
    main()