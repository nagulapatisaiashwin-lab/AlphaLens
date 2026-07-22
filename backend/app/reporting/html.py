"""
HTML report generation for AlphaLens.
"""

from __future__ import annotations

from pathlib import Path

from app.reporting.components import (
    build_dataset_card,
    build_footer,
    build_header,
    build_kpi_grid,
    build_metric_card,
    build_metric_grid,
)
from app.reporting.formatters import format_metric
from app.reporting.templates import render_page


def generate_html_report(
    result,
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

    # Header
    body += build_header(
        "AlphaLens",
        "Professional Quantitative Strategy Tearsheet",
    )

    # KPI Cards
    body += build_kpi_grid(
        [
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

    # Dataset
    body += build_dataset_card(
        result.dataset_type,
        len(result.returns),
    )

    # Metric Grid
    body += build_metric_grid(
        [
            build_metric_card(
                "Performance",
                performance,
            ),
            build_metric_card(
                "Risk",
                risk,
            ),
            build_metric_card(
                "Statistics",
                statistics,
            ),
            build_metric_card(
                "Distribution",
                distribution,
            ),
        ]
    )

    # Footer
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