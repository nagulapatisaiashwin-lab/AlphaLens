"""
AlphaLens Monthly Returns Heatmap
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go




MONTH_NAMES = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec",
]


def plot_monthly_heatmap(
    returns: pd.Series,
    filename: str = "monthly_heatmap.html",
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

    fig = go.Figure(
        data=go.Heatmap(
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
            colorbar=dict(title="Return %"),
        )
    )

    fig.update_layout(
        title="Monthly Returns Heatmap",
        xaxis_title="Month",
        yaxis_title="Year",
    )

   

    return fig