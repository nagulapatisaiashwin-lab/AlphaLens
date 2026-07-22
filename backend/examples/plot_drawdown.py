"""
Generate AlphaLens Drawdown Chart
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.io.loader import load_csv
from app.visualization.drawdown import plot_drawdown


def main():

    df = load_csv("examples/realistic_returns.csv")

    plot_drawdown(df)


if __name__ == "__main__":
    main()