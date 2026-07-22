"""
AlphaLens Analysis Pipeline
"""

from __future__ import annotations

from pathlib import Path

from app.core.result import AnalysisResult

from app.io.loader import load_csv
from app.io.detector import detect_dataset_type
from app.io.normalizer import extract_returns

from app.report import analyze_strategy, print_report

from app.reporting.html import generate_html_report

from app.visualization.registry import generate_all_charts


def run(csv_path: str | Path) -> AnalysisResult:
    """
    Execute the complete AlphaLens pipeline.
    """

    csv_path = Path(csv_path)

    # Load data
    df = load_csv(csv_path)

    # Detect dataset type
    dataset_type = detect_dataset_type(df)

    # Extract returns
    returns = extract_returns(df)

    # Compute analytics
    metrics = analyze_strategy(returns)

    # Create analysis result
    result = AnalysisResult(
        dataset_type=dataset_type,
        data=df,
        returns=returns,
        metrics=metrics,
    )

    # Console report
    print(f"\nDetected Dataset Type : {result.dataset_type}")
    print(f"Observations          : {len(result.returns)}\n")

    print_report(result.metrics)

    # Generate charts
    print("\nGenerating visualizations...\n")

    generate_all_charts(result.data)

    # Generate HTML report
    print("\nGenerating HTML report...\n")

    generate_html_report(result)

    print("\nAlphaLens analysis completed successfully.")

    return result