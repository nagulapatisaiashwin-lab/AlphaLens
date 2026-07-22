"""
AlphaLens Equity Curve Visualization
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from app.visualization.base import (
    create_figure,
    apply_time_controls,
)
from app.visualization.theme import THEME


def plot_equity_curve(df: pd.DataFrame) -> go.Figure:
    """
    Create an interactive equity curve chart.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame indexed by Date containing Portfolio Value and
        optionally Benchmark Value.

    Returns
    -------
    go.Figure
        Plotly figure object.
    """

    fig = create_figure("Portfolio vs Benchmark")

    # Apply common time controls
    apply_time_controls(fig)

    # Portfolio
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Portfolio Value"],
            mode="lines",
            name="Portfolio",
            line=dict(
                color=THEME["portfolio"],
                width=2.5,
            ),
        )
    )

    # Benchmark (optional)
    if "Benchmark Value" in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["Benchmark Value"],
                mode="lines",
                name="Benchmark",
                line=dict(
                    color=THEME["benchmark"],
                    width=2,
                    dash="dot",
                ),
            )
        )

    # Legend
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
    )

    # Axis labels
    fig.update_xaxes(
        title="Date",
    )

    fig.update_yaxes(
        title="Portfolio Value",
        tickformat=",.0f",
    )

    return fig