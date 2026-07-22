"""
Generate Return Distribution Chart
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.io.loader import load_csv
from app.io.normalizer import extract_returns
from app.visualization.distribution import plot_return_distribution


def main():

    df = load_csv("examples/realistic_returns.csv")

    returns = extract_returns(df)

    plot_return_distribution(returns)


if __name__ == "__main__":
    main()