"""
AlphaLens Analysis Pipeline
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from app.core.result import AnalysisResult

from app.io import (
    load_file,
    validate_dataframe,
    detect_schema,
    normalize_dataframe,
    detect_frequency,
)

from app.preprocessing import (
    extract_returns,
    extract_benchmark_returns,
)

from app.report import (
    analyze_strategy,
    print_report,
)

from app.reporting.html import generate_html_report

from app.visualization.registry import generate_all_charts


def run(
    file_path: str | Path,
    factor_data: pd.DataFrame | None = None,
    generate_charts: bool = True,
    generate_html: bool = True,
    verbose: bool = True,
) -> AnalysisResult:
    """
    Execute the complete AlphaLens pipeline.
    """

    file_path = Path(file_path)

    # -------------------------
    # Ingestion
    # -------------------------

    df = load_file(file_path)

    validate_dataframe(df)

    schema = detect_schema(df)

    df = normalize_dataframe(df, schema)

    frequency = detect_frequency(df)

    # -------------------------
    # Preprocessing
    # -------------------------

    portfolio_returns = extract_returns(df)

    benchmark_returns = extract_benchmark_returns(df)

    # -------------------------
    # Analytics
    # -------------------------

    metrics = analyze_strategy(
        portfolio_returns,
        benchmark_returns=benchmark_returns,
        factor_data=factor_data,
        periods_per_year=frequency.annualization_factor,
    )

    # -------------------------
    # Result
    # -------------------------

    result = AnalysisResult(
        dataset_type="Portfolio Dataset",
        frequency=frequency,
        data=df,
        returns=portfolio_returns,
        metrics=metrics,
    )

    # -------------------------
    # Console Report
    # -------------------------

    if verbose:

        print("\nDetected Schema")
        print(f"Date Column      : {schema.date}")
        print(f"Portfolio Column : {schema.portfolio}")

        if schema.benchmark is not None:
            print(f"Benchmark Column : {schema.benchmark}")

        print(f"Detected Frequency : {frequency.name}")
        print(f"Observations       : {len(result.returns)}\n")

        print_report(result.metrics)

    # -------------------------
    # Visualization
    # -------------------------

    if generate_charts:

        if verbose:
            print("\nGenerating visualizations...\n")

        figures = generate_all_charts(
            result.data,
            factor_results=result.metrics.get("Factor Analysis"),
        )

        result.charts = figures

    # -------------------------
    # HTML Report
    # -------------------------

    if generate_html:

        if verbose:
            print("\nGenerating HTML report...\n")

        generate_html_report(
            result,
            result.charts,
        )

    if verbose:
        print("\nAlphaLens analysis completed successfully.")

    return result