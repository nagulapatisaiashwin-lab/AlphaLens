"""
Utility functions for AlphaLens visualizations.
"""

from __future__ import annotations

from pathlib import Path

import plotly.graph_objects as go


OUTPUT_DIR = Path("outputs/charts")


def ensure_output_dir() -> None:
    """
    Create the output directory if it does not exist.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_figure(fig: go.Figure, filename: str) -> Path:
    """
    Save a Plotly figure as an HTML file.

    Parameters
    ----------
    fig : go.Figure
        Plotly figure to save.
    filename : str
        Output filename (e.g. "equity_curve.html").

    Returns
    -------
    Path
        Path to the saved file.
    """
    ensure_output_dir()

    output_path = OUTPUT_DIR / filename

    fig.write_html(output_path)

    print(f"Chart saved to: {output_path}")

    return output_path