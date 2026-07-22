"""
AlphaLens Data Loader

Responsible solely for reading supported portfolio datasets into a pandas
DataFrame.

Responsibilities
----------------
- Load CSV files
- Load Excel files
- Return raw DataFrames

Non-Responsibilities
--------------------
- Schema detection
- Data validation
- Column renaming
- Date parsing
- Frequency detection
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


SUPPORTED_EXTENSIONS = {
    ".csv",
    ".xlsx",
    ".xls",
}

CSV_ENCODINGS = (
    "utf-8",
    "utf-8-sig",
    "cp1252",
    "latin1",
)


def load_file(file_path: str | Path) -> pd.DataFrame:
    """
    Load a supported dataset into a pandas DataFrame.

    Parameters
    ----------
    file_path : str | Path
        Path to the dataset.

    Returns
    -------
    pd.DataFrame
        Raw DataFrame preserving the original columns and values.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.

    ValueError
        If the file format is unsupported or cannot be read.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    extension = path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        supported = ", ".join(sorted(SUPPORTED_EXTENSIONS))
        raise ValueError(
            f"Unsupported file format '{extension}'. "
            f"Supported formats: {supported}"
        )

    if extension == ".csv":
        return _load_csv(path)

    return _load_excel(path)


def _load_csv(path: Path) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    The loader attempts multiple common encodings to maximize compatibility
    with broker exports and spreadsheet software.
    """

    last_error = None

    for encoding in CSV_ENCODINGS:
        try:
            df = pd.read_csv(
                path,
                encoding=encoding,
                sep=None,
                engine="python",
            )

            if df.empty:
                raise ValueError(f"CSV file is empty: {path}")

            return df

        except UnicodeDecodeError as exc:
            last_error = exc

    raise ValueError(
        f"Unable to read CSV file '{path.name}'. "
        "The file encoding is not supported."
    ) from last_error


def _load_excel(path: Path) -> pd.DataFrame:
    """
    Load an Excel workbook into a pandas DataFrame.
    """

    try:
        df = pd.read_excel(path)

    except Exception as exc:
        raise ValueError(
            f"Unable to read Excel file '{path.name}'."
        ) from exc

    if df.empty:
        raise ValueError(f"Excel file is empty: {path}")

    return df