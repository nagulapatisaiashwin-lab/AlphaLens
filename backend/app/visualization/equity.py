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



def plot_equity_curve(
    df: pd.DataFrame,
) -> go.Figure:
    """
    Create portfolio equity curve chart.

    Equity curve should represent only the
    portfolio value through time.

    Benchmark comparison is handled separately
    by benchmark_comparison.py.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame indexed by Date containing
        Portfolio Value column.

    Returns
    -------
    go.Figure
        Plotly figure object.
    """


    fig = create_figure(
        "Portfolio Equity Curve"
    )


    apply_time_controls(fig)



    # -----------------------------
    # Portfolio Equity
    # -----------------------------

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



    # -----------------------------
    # Layout
    # -----------------------------

    fig.update_layout(

        legend=dict(

            orientation="h",

            yanchor="bottom",

            y=1.02,

            xanchor="right",

            x=1,

        ),

        margin=dict(

            l=60,

            r=30,

            t=45,

            b=50,

        ),

    )



    fig.update_xaxes(

        title="Date",

    )


    fig.update_yaxes(

        title="Portfolio Value",

        tickformat=",.0f",

    )


    return fig