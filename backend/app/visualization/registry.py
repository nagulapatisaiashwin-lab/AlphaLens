"""
Visualization registry for AlphaLens.
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from app.io.normalizer import extract_returns
from app.visualization.benchmark import plot_benchmark_comparison
from app.visualization.drawdown import plot_drawdown
from app.visualization.equity import plot_equity_curve
from app.visualization.heatmap import plot_monthly_heatmap
from app.visualization.utils import save_figure


def generate_all_charts(
    df: pd.DataFrame,
    save: bool = True,
) -> dict[str, go.Figure]:
    """
    Generate all visualizations.

    Parameters
    ----------
    df : pd.DataFrame

    save : bool, default=True
        Save charts as standalone HTML files.

    Returns
    -------
    dict[str, go.Figure]
        Dictionary of Plotly figures.
    """

    figures: dict[str, go.Figure] = {}

    print("Generating equity curve...")
    figures["equity"] = plot_equity_curve(df)

    print("Generating drawdown...")
    figures["drawdown"] = plot_drawdown(df)

    print("Generating monthly heatmap...")
    returns = extract_returns(df)
    figures["heatmap"] = plot_monthly_heatmap(returns)

    print("Generating benchmark comparison...")
    figures["benchmark"] = plot_benchmark_comparison(df)

    if save:
        save_figure(figures["equity"], "equity_curve.html")
        save_figure(figures["drawdown"], "drawdown.html")
        save_figure(figures["heatmap"], "monthly_heatmap.html")
        save_figure(figures["benchmark"], "benchmark_comparison.html")

    print("Visualization generation complete.")

    return figures