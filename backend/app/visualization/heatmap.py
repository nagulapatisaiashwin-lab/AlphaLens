"""
AlphaLens Monthly Returns Heatmap
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from app.visualization.base import create_figure
from app.visualization.theme import THEME


MONTH_NAMES = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec",
]


def plot_monthly_heatmap(
    returns: pd.Series,
) -> go.Figure:
    """
    Generate a monthly returns heatmap.
    """

    monthly_returns = (1 + returns).resample("ME").prod() - 1

    heatmap = pd.DataFrame(
        {
            "Year": monthly_returns.index.year,
            "Month": monthly_returns.index.month,
            "Return": monthly_returns.values * 100,
        }
    )

    table = heatmap.pivot(
        index="Year",
        columns="Month",
        values="Return",
    )

    table = table.reindex(columns=range(1, 13))
    table.columns = MONTH_NAMES

    fig = create_figure("Monthly Returns Heatmap")

    fig.add_trace(
        go.Heatmap(
            z=table.values,
            x=table.columns,
            y=table.index.astype(str),
            text=table.round(2).fillna("").values,
            texttemplate="%{text}",
            hovertemplate=(
                "Year: %{y}<br>"
                "Month: %{x}<br>"
                "Return: %{z:.2f}%<extra></extra>"
            ),
            colorscale="RdYlGn",
            colorbar=dict(
                title="Return %",
                tickfont=dict(color=THEME["muted"]),
                title_font=dict(color=THEME["text"]),
            ),
        )
    )

    fig.update_layout(
        hovermode="closest",
    )

    fig.update_xaxes(
        title="Month",
        showgrid=False,
    )

    fig.update_yaxes(
        title="Year",
        showgrid=False,
    )

    return fig