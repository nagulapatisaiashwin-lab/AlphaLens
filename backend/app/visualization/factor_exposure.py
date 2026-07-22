"""
Factor exposure visualization for AlphaLens.
"""

from __future__ import annotations

import plotly.graph_objects as go


def plot_factor_exposure(
    factor_results: dict[str, dict],
) -> go.Figure:
    """
    Plot factor exposures from the richest available model.

    Priority:
        1. Carhart 4 Factor
        2. Fama-French 3 Factor
        3. CAPM
    """

    if not factor_results:
        raise ValueError("No factor analysis results available.")

    if "Carhart 4 Factor" in factor_results:
        model_name = "Carhart 4 Factor"
        metric_order = [
            "Market Beta",
            "SMB",
            "HML",
            "Momentum",
            "Alpha",
        ]

    elif "Fama-French 3 Factor" in factor_results:
        model_name = "Fama-French 3 Factor"
        metric_order = [
            "Market Beta",
            "SMB",
            "HML",
            "Alpha",
        ]

    elif "CAPM" in factor_results:
        model_name = "CAPM"
        metric_order = [
            "Market Beta",
            "Alpha",
        ]

    else:
        raise ValueError("No supported factor model found.")

    metrics = factor_results[model_name]

    labels = []
    values = []

    for metric in metric_order:
        if metric in metrics:
            labels.append(metric)
            values.append(metrics[metric])

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=values,
            y=labels,
            orientation="h",
            text=[f"{v:.3f}" for v in values],
            textposition="outside",
            marker=dict(
                color="#3B82F6",
                line=dict(
                    color="white",
                    width=1,
                ),
            ),
            hovertemplate="<b>%{y}</b><br>Coefficient: %{x:.4f}<extra></extra>",
        )
    )

    fig.add_vline(
        x=0,
        line_dash="dash",
        line_width=2,
        line_color="white",
    )

    fig.update_layout(
        title=dict(
            text=f"{model_name} Factor Exposure",
            x=0.5,
            font=dict(
                size=22,
                color="white",
            ),
        ),

        template="plotly_dark",

        paper_bgcolor="#0B0F19",
        plot_bgcolor="#0B0F19",

        font=dict(
            color="white",
            size=14,
        ),

        xaxis=dict(
            title="Factor Loading",
            gridcolor="#2D3748",
            zeroline=False,
            showline=True,
            linecolor="#666666",
        ),

        yaxis=dict(
            title="",
            gridcolor="#2D3748",
            showline=False,
        ),

        margin=dict(
            l=90,
            r=60,
            t=80,
            b=60,
        ),

        height=500,
    )

    return fig