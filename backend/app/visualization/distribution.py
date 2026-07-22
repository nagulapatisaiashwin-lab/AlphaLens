"""
AlphaLens Return Distribution Visualization
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.stats import gaussian_kde

from app.visualization.base import create_figure
from app.visualization.theme import THEME


def plot_return_distribution(
    returns: pd.Series,
    bins: int = 40,
) -> go.Figure:
    """
    Plot return distribution with histogram and KDE curve.
    """

    returns = returns.dropna()

    returns_pct = returns * 100

    fig = create_figure("Return Distribution")

    # -----------------------------------------------------
    # Histogram
    # -----------------------------------------------------

    fig.add_trace(
        go.Histogram(
            x=returns_pct,
            nbinsx=bins,
            name="Returns",
            marker=dict(
                color=THEME["portfolio"],
            ),
            opacity=0.65,
        )
    )

    # -----------------------------------------------------
    # KDE Curve
    # -----------------------------------------------------

    kde = gaussian_kde(returns_pct)

    x = np.linspace(
        returns_pct.min(),
        returns_pct.max(),
        300,
    )

    y = kde(x)

    # Scale KDE to histogram frequency
    bin_width = (returns_pct.max() - returns_pct.min()) / bins
    y = y * len(returns_pct) * bin_width

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            name="Density",
            line=dict(
                width=3,
            ),
        )
    )

    # -----------------------------------------------------
    # Statistics
    # -----------------------------------------------------

    mean = returns_pct.mean()
    median = returns_pct.median()
    std = returns_pct.std()

    fig.add_vline(
        x=mean,
        line_dash="dash",
        line_color="green",
        annotation_text="Mean",
    )

    fig.add_vline(
        x=median,
        line_dash="dash",
        line_color="blue",
        annotation_text="Median",
    )

    fig.add_vline(
        x=mean + std,
        line_dash="dot",
        line_color="orange",
    )

    fig.add_vline(
        x=mean - std,
        line_dash="dot",
        line_color="orange",
    )

    # -----------------------------------------------------
    # Layout
    # -----------------------------------------------------

    fig.update_layout(
        bargap=0.05,
        hovermode="x unified",
    )

    fig.update_xaxes(
        title="Daily Return (%)",
    )

    fig.update_yaxes(
        title="Frequency",
    )

    return fig