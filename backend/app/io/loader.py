"""
AlphaLens Data Loader
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_csv(file_path: str | Path) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    Automatically converts a Date column into a DatetimeIndex if present.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.suffix.lower() != ".csv":
        raise ValueError("Only CSV files are currently supported.")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("CSV file is empty.")

    # Automatically parse dates
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.set_index("Date")
        df = df.sort_index()

    return df