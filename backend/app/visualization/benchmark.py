"""
AlphaLens Benchmark Comparison Visualization
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from app.visualization.base import create_figure
from app.visualization.theme import THEME



def plot_benchmark_comparison(
    df: pd.DataFrame,
    filename: str = "benchmark_comparison.html",
) -> go.Figure:
    """
    Compare portfolio and benchmark performance.
    """

    if "Benchmark Value" not in df.columns:
        raise ValueError("Dataset does not contain a 'Benchmark Value' column.")

    portfolio = df["Portfolio Value"] / df["Portfolio Value"].iloc[0] * 100
    benchmark = df["Benchmark Value"] / df["Benchmark Value"].iloc[0] * 100

    fig = create_figure("Portfolio vs Benchmark")

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=portfolio,
            mode="lines",
            name="Portfolio",
            line=dict(
                color=THEME["portfolio"],
                width=2.5,
            ),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=benchmark,
            mode="lines",
            name="Benchmark",
            line=dict(
                color=THEME["benchmark"],
                width=2,
                dash="dash",
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
    )

    fig.update_yaxes(
        title="Normalized Value (Start = 100)",
    )

    

    return fig