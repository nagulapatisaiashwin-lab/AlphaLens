"""
Rolling analytics visualizations for AlphaLens.
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from app.visualization.base import create_figure
from app.visualization.theme import THEME
from app.visualization.utils import save_figure


def plot_rolling_metric(
    series: pd.Series,
    dates: pd.Series,
    title: str,
    y_label: str,
    filename: str,
    color: str | None = None,
) -> None:
    """
    Plot any rolling metric.
    """

    fig = create_figure(title)

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=series,
            mode="lines",
            name=title,
            line=dict(
                color=color or THEME["rolling"],
                width=2,
            ),
        )
    )

    fig.update_xaxes(title="Date")
    fig.update_yaxes(title=y_label)

    save_figure(fig, filename)