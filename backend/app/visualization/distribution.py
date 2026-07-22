"""
Return Distribution Visualization
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from app.visualization.base import create_figure
from app.visualization.theme import THEME
from app.visualization.utils import save_figure


def plot_return_distribution(
    returns: pd.Series,
    filename: str = "distribution.html",
) -> None:
    """
    Plot the distribution of portfolio returns.
    """

    fig = create_figure("Return Distribution")

    fig.add_trace(
        go.Histogram(
            x=returns * 100,
            nbinsx=50,
            name="Returns",
            opacity=0.8,
        )
    )

    mean = returns.mean() * 100
    median = returns.median() * 100

    fig.add_vline(
        x=mean,
        line_dash="dash",
        annotation_text="Mean",
    )

    fig.add_vline(
        x=median,
        line_dash="dot",
        annotation_text="Median",
    )

    fig.update_xaxes(title="Daily Return (%)")
    fig.update_yaxes(title="Frequency")

    save_figure(fig, filename)