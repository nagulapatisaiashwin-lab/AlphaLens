"""
AlphaLens Rolling Metrics Visualization
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from app.analytics.rolling import (
    rolling_sharpe,
    rolling_volatility,
)
from app.visualization.base import create_figure


def plot_rolling_metrics(
    returns: pd.Series,
    window: int = 63,
) -> go.Figure:
    """
    Plot rolling performance metrics.
    """

    sharpe = rolling_sharpe(returns, window)
    volatility = rolling_volatility(returns, window)

    rolling_return = (
        (1 + returns)
        .rolling(window)
        .apply(lambda x: x.prod() - 1, raw=False)
        * 100
    )

    fig = create_figure(f"Rolling Metrics ({window}D)")

    fig.add_trace(
        go.Scatter(
            x=returns.index,
            y=sharpe,
            name="Rolling Sharpe",
            mode="lines",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=returns.index,
            y=volatility,
            name="Rolling Volatility",
            mode="lines",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=returns.index,
            y=rolling_return,
            name="Rolling Return (%)",
            mode="lines",
        )
    )

    fig.update_layout(
        hovermode="x unified",
    )

    fig.update_xaxes(title="Date")
    fig.update_yaxes(title="Value")

    return fig