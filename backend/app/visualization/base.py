"""
Base utilities for AlphaLens visualizations.
"""

from __future__ import annotations

import plotly.graph_objects as go

from app.visualization.theme import THEME


def create_figure(title: str) -> go.Figure:
    """
    Create a Plotly figure with the AlphaLens theme applied.
    """

    fig = go.Figure()

    fig.update_layout(

        title={
            "text": title,
            "x": 0.02,
            "xanchor": "left",
            "font": {
                "size": THEME["title_size"],
            },
        },

        width=THEME["width"],
        height=THEME["height"],

        plot_bgcolor=THEME["background"],
        paper_bgcolor=THEME["paper"],

        font={
            "family": THEME["font_family"],
            "size": THEME["font_size"],
        },

        margin=dict(
            l=THEME["margin_left"],
            r=THEME["margin_right"],
            t=THEME["margin_top"],
            b=THEME["margin_bottom"],
        ),

        hovermode="x unified",

        legend=dict(
            bgcolor=THEME["legend_bg"],
        ),
    )

    fig.update_xaxes(

        showgrid=True,
        gridcolor=THEME["grid"],
        zeroline=False,
        linecolor=THEME["axis"],
    )

    fig.update_yaxes(

        showgrid=True,
        gridcolor=THEME["grid"],
        zeroline=False,
        linecolor=THEME["axis"],
    )

    return fig