"""
AlphaLens Command Line Interface
"""

from pathlib import Path
import sys

import pandas as pd

from app.pipeline import run


def main():

    if len(sys.argv) not in (2, 3):
        print("Usage:")
        print("python analyze.py <portfolio_file>")
        print("python analyze.py <portfolio_file> <factor_file>")
        return

    portfolio_path = Path(sys.argv[1])

    factor_data = None

    if len(sys.argv) == 3:

        factor_path = Path(sys.argv[2])

        try:
            factor_data = pd.read_csv(
                factor_path,
                parse_dates=True,
                index_col=0,
            )

        except Exception as e:
            print(f"\nFailed to load factor file: {e}")
            return

    try:

        run(
            portfolio_path,
            factor_data=factor_data,
            generate_charts=True,
            generate_html=True,
            verbose=True,
        )

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()