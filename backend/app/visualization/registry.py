"""
Visualization registry for AlphaLens.
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from app.io.normalizer import extract_returns
from app.visualization.benchmark import plot_benchmark_comparison
from app.visualization.distribution import plot_return_distribution
from app.visualization.drawdown import plot_drawdown
from app.visualization.equity import plot_equity_curve
from app.visualization.heatmap import plot_monthly_heatmap
from app.visualization.rolling import plot_rolling_metrics
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

    # ------------------------------------------------------
    # Equity Curve
    # ------------------------------------------------------

    print("Generating equity curve...")
    figures["equity"] = plot_equity_curve(df)

    # ------------------------------------------------------
    # Drawdown
    # ------------------------------------------------------

    print("Generating drawdown...")
    figures["drawdown"] = plot_drawdown(df)

    # ------------------------------------------------------
    # Returns
    # ------------------------------------------------------

    returns = extract_returns(df)

    # ------------------------------------------------------
    # Monthly Heatmap
    # ------------------------------------------------------

    print("Generating monthly heatmap...")
    figures["heatmap"] = plot_monthly_heatmap(returns)

    # ------------------------------------------------------
    # Return Distribution
    # ------------------------------------------------------

    print("Generating return distribution...")
    figures["distribution"] = plot_return_distribution(returns)

    # ------------------------------------------------------
    # Benchmark Comparison
    # ------------------------------------------------------

    print("Generating benchmark comparison...")
    figures["benchmark"] = plot_benchmark_comparison(df)

    # ------------------------------------------------------
    # Rolling Metrics
    # ------------------------------------------------------

    print("Generating rolling metrics...")
    figures["rolling"] = plot_rolling_metrics(returns)

    # ------------------------------------------------------
    # Save Figures
    # ------------------------------------------------------

    if save:
        save_figure(figures["equity"], "equity_curve.html")
        save_figure(figures["drawdown"], "drawdown.html")
        save_figure(figures["heatmap"], "monthly_heatmap.html")
        save_figure(figures["distribution"], "return_distribution.html")
        
        save_figure(figures["rolling"], "rolling_metrics.html")

    print("Visualization generation complete.")

    return figures