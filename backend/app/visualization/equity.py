"""
AlphaLens Equity Curve Visualization
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from app.visualization.base import create_figure
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

    fig.update_layout(
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
    )

    fig.update_xaxes(
        title="Date",
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=[
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=3, label="3M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="1Y", step="year", stepmode="backward"),
                dict(step="all", label="All"),
            ]
        ),
    )

    fig.update_yaxes(
        title="Portfolio Value",
        tickformat=",.0f",
    )

    return fig