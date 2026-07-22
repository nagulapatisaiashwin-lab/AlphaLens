"""
HTML report generation for AlphaLens.
"""

from __future__ import annotations

from pathlib import Path

import plotly.io as pio

from app.reporting.components import (
    build_chart_card,
    build_dataset_card,
    build_footer,
    build_header,
    build_kpi_grid,
    build_metric_card,
    build_metric_grid,
)
from app.reporting.formatters import format_metric
from app.reporting.templates import render_page


def _embed_plotly_chart(figure, include_plotlyjs: bool = False) -> str:
    """
    Convert a Plotly figure into embeddable HTML.
    """

    return pio.to_html(
        figure,
        full_html=False,
        include_plotlyjs="cdn" if include_plotlyjs else False,
        config={"responsive": True},
    )


def generate_html_report(
    result,
    figures: dict[str, object],
    output_path: str = "outputs/reports/tearsheet.html",
) -> None:
    """
    Generate AlphaLens HTML tearsheet.
    """

    performance = result.metrics["Performance"]
    risk = result.metrics["Risk"]
    statistics = result.metrics["Statistics"]
    distribution = result.metrics["Distribution"]

    body = ""

    # ======================================================
    # Header
    # ======================================================

    body += build_header(
        "AlphaLens",
        "Professional Quantitative Strategy Tearsheet",
    )

    # ======================================================
    # KPI Cards
    # ======================================================

    kpis = [
        (
            "Total Return",
            format_metric(
                "Total Return",
                performance["Total Return"],
            ),
        ),
        (
            "Annual Return",
            format_metric(
                "Annualized Return",
                performance["Annualized Return"],
            ),
        ),
    ]

    # Add CAGR if available
    if "CAGR" in performance:
        kpis.append(
            (
                "CAGR",
                format_metric(
                    "CAGR",
                    performance["CAGR"],
                ),
            )
        )

    kpis.extend(
        [
            (
                "Sharpe Ratio",
                format_metric(
                    "Sharpe Ratio",
                    performance["Sharpe Ratio"],
                ),
            ),
            (
                "Max Drawdown",
                format_metric(
                    "Maximum Drawdown",
                    risk["Maximum Drawdown"],
                ),
            ),
        ]
    )

    body += build_kpi_grid(kpis)

    # ======================================================
    # Dataset Information
    # ======================================================

    body += build_dataset_card(
        result.dataset_type,
        len(result.returns),
    )

    # ======================================================
    # Equity Curve
    # ======================================================

    if "equity" in figures:
        body += build_chart_card(
            "Equity Curve",
            _embed_plotly_chart(
                figures["equity"],
                include_plotlyjs=True,
            ),
        )

    # ======================================================
    # Drawdown 
    # ======================================================

    chart_cards = []

    if "drawdown" in figures:
        chart_cards.append(
            build_chart_card(
                "Portfolio Drawdown",
                _embed_plotly_chart(
                    figures["drawdown"],
                ),
            )
        )

    

    if chart_cards:
        body += build_metric_grid(chart_cards)

    # ======================================================
    # Monthly Heatmap
    # ======================================================

    if "heatmap" in figures:
        body += build_chart_card(
            "Monthly Returns Heatmap",
            _embed_plotly_chart(
                figures["heatmap"],
            ),
        )
        
    # ======================================================
# Rolling Metrics
# ======================================================

    if "rolling" in figures:
        body += build_chart_card(
            "Rolling Metrics",
            _embed_plotly_chart(
            figures["rolling"],
        ),
    )   
    
    # ======================================================
# Return Distribution
# ======================================================

    if "distribution" in figures:
        body += build_chart_card(
            "Return Distribution",
            _embed_plotly_chart(
            figures["distribution"],
        ),
    )     

    # ======================================================
    # Metric Tables
    # ======================================================

    body += build_metric_grid(
        [
            build_metric_card(
                "Performance Metrics",
                performance,
            ),
            build_metric_card(
                "Risk Metrics",
                risk,
            ),
        ]
    )

    body += build_metric_grid(
        [
            build_metric_card(
                "Statistics",
                statistics,
            ),
            build_metric_card(
                "Distribution Metrics",
                distribution,
            ),
        ]
    )

    # ======================================================
    # Footer
    # ======================================================

    body += build_footer()

    html = render_page(
        "AlphaLens Strategy Report",
        body,
    )

    output = Path(output_path)

    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output.write_text(
        html,
        encoding="utf-8",
    )

    print(f"HTML report saved to: {output}")