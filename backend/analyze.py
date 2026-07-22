"""
AlphaLens Command Line Interface
"""

from pathlib import Path
import sys

from app.pipeline import run


def main():

    if len(sys.argv) != 2:
        print("Usage:")
        print("python analyze.py <csv_file>")
        return

    csv_path = Path(sys.argv[1])

    try:

        run(csv_path)

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()