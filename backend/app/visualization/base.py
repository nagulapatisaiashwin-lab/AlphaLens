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
                "color": THEME["text"],
            },
        },
        width=THEME["width"],
        height=THEME["height"],
        plot_bgcolor=THEME["background"],
        paper_bgcolor=THEME["paper"],
        font={
            "family": THEME["font_family"],
            "size": THEME["font_size"],
            "color": THEME["text"],
        },
        margin=dict(
            l=THEME["margin_left"],
            r=THEME["margin_right"],
            t=THEME["margin_top"],
            b=THEME["margin_bottom"],
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor=THEME["surface"],
            font_size=13,
            font_color=THEME["text"],
            bordercolor=THEME["border"],
        ),
        legend=dict(
            orientation="h",
            y=1.08,
            x=0,
            bgcolor="rgba(0,0,0,0)",
            font=dict(
                color=THEME["muted"],
            ),
        ),
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor=THEME["grid"],
        zeroline=False,
        linecolor=THEME["axis"],
        tickfont=dict(
            color=THEME["muted"],
        ),
        title_font=dict(
            color=THEME["text"],
        ),
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=THEME["grid"],
        zeroline=False,
        linecolor=THEME["axis"],
        tickfont=dict(
            color=THEME["muted"],
        ),
        title_font=dict(
            color=THEME["text"],
        ),
    )

    return fig


def apply_time_controls(
    fig: go.Figure,
    *,
    show_rangeslider: bool = True,
) -> None:
    """
    Apply a consistent time navigation control to a figure.
    """

    fig.update_xaxes(
        rangeslider_visible=show_rangeslider,
        rangeselector=dict(
            bgcolor="#1F2937",
            activecolor="#374151",
            bordercolor="#4B5563",
            borderwidth=1,
            font=dict(
                color="#F8FAFC",
                size=12,
            ),
            buttons=[
                dict(
                    count=1,
                    label="1M",
                    step="month",
                    stepmode="backward",
                ),
                dict(
                    count=3,
                    label="3M",
                    step="month",
                    stepmode="backward",
                ),
                dict(
                    count=6,
                    label="6M",
                    step="month",
                    stepmode="backward",
                ),
                dict(
                    count=1,
                    label="YTD",
                    step="year",
                    stepmode="todate",
                ),
                dict(
                    count=1,
                    label="1Y",
                    step="year",
                    stepmode="backward",
                ),
                dict(
                    step="all",
                    label="All",
                ),
            ],
        ),
    )