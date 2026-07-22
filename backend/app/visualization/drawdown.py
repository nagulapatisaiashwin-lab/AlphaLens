"""
AlphaLens Drawdown Visualization
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from app.visualization.base import (
    create_figure,
    apply_time_controls,
)
from app.visualization.theme import THEME


def plot_drawdown(df: pd.DataFrame) -> go.Figure:
    """
    Plot portfolio drawdown.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    go.Figure
    """

    equity = df["Portfolio Value"]

    running_peak = equity.cummax()

    drawdown = (equity / running_peak - 1.0) * 100

    fig = create_figure("Portfolio Drawdown")

    # Apply common time controls (without range slider)
    apply_time_controls(
        fig,
        show_rangeslider=False,
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=drawdown,
            mode="lines",
            name="Drawdown",
            line=dict(
                color=THEME["drawdown"],
                width=2,
            ),
            fill="tozeroy",
        )
    )

    fig.update_xaxes(
        title="Date",
    )

    fig.update_yaxes(
        title="Drawdown (%)",
        ticksuffix="%",
    )

    return fig