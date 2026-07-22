"""
AlphaLens Monthly Returns Heatmap
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from app.visualization.base import create_figure



def plot_monthly_heatmap(
    returns: pd.Series,
) -> go.Figure:


    monthly = (
        returns
        .resample("ME")
        .apply(lambda x: (1 + x).prod() - 1)
    )


    table = (
        monthly
        .to_frame("Return")
        .assign(
            Year=lambda x: x.index.year,
            Month=lambda x: x.index.month,
        )
        .pivot(
            index="Year",
            columns="Month",
            values="Return",
        )
    )


    fig = create_figure(
        ""
    )


    fig.add_trace(

        go.Heatmap(

            z=table.values * 100,

            x=[
                str(m)
                for m in table.columns
            ],

            y=[
                str(y)
                for y in table.index
            ],

            text=[
                [
                    f"{v:.2f}"
                    for v in row
                ]

                for row in table.values * 100
            ],

            texttemplate="%{text}%",

            colorbar=dict(
                title="Return %",
            ),

            hovertemplate=
            "Year: %{y}<br>"
            "Month: %{x}<br>"
            "Return: %{z:.2f}%<extra></extra>",

        )

    )


    fig.update_layout(

        height=320,

        margin=dict(
            l=60,
            r=40,
            t=20,
            b=40,
        ),

    )


    fig.update_xaxes(
        title="Month"
    )


    fig.update_yaxes(
        title="Year"
    )


    return fig