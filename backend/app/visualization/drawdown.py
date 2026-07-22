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


def plot_drawdown(
    df: pd.DataFrame,
) -> go.Figure:


    portfolio = df["Portfolio Value"]


    peak = portfolio.cummax()


    drawdown = (
        portfolio / peak - 1
    ) * 100



    fig = create_figure(
        ""
    )


    apply_time_controls(fig)



    fig.add_trace(

        go.Scatter(

            x=drawdown.index,

            y=drawdown,

            mode="lines",

            name="Drawdown",

            fill="tozeroy",

        )

    )



    fig.update_layout(

        height=320,


        margin=dict(

            l=60,

            r=30,

            t=20,

            b=45,

        ),


    )



    fig.update_xaxes(
        title="Date"
    )


    fig.update_yaxes(

        title="Drawdown (%)",

        ticksuffix="%",

        rangemode="tozero",

    )


    return fig