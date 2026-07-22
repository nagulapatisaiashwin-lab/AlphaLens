"""
AlphaLens Strategy Report
"""

from __future__ import annotations

import pandas as pd

from app.analytics.returns import (
    total_return,
    annualized_return,
    volatility,
)

from app.analytics.drawdown import (
    max_drawdown,
)

from app.analytics.performance import (
    sharpe_ratio,
)

from app.analytics.statistics import (
    mean_return,
    median_return,
    best_day,
    worst_day,
    positive_days,
    negative_days,
    win_rate,
)

from app.analytics.distribution import (
    standard_deviation,
    skewness,
    kurtosis,
    percentile,
    interquartile_range,
)

from app.analytics.risk import (
    downside_deviation,
    sortino_ratio,
    calmar_ratio,
    value_at_risk,
    conditional_value_at_risk,
)

from app.analytics.benchmark import (
    correlation,
    beta,
    alpha,
    tracking_error,
    active_return,
    information_ratio,
)

from app.analytics.factors import (
    factor_analysis,
)


def analyze_strategy(
    portfolio_returns: pd.Series,
    benchmark_returns: pd.Series | None = None,
    factor_data: pd.DataFrame | None = None,
    periods_per_year: int = 252,
) -> dict:
    """
    Generate a structured strategy report.
    """

    report = {

        "Performance": {
            "Total Return": total_return(portfolio_returns),
            "Annualized Return": annualized_return(
                portfolio_returns,
                periods_per_year=periods_per_year,
            ),
            "Sharpe Ratio": sharpe_ratio(
                portfolio_returns,
                periods_per_year=periods_per_year,
            ),
        },

        "Risk": {
            "Annualized Volatility": volatility(
                portfolio_returns,
                periods_per_year=periods_per_year,
            ),
            "Maximum Drawdown": max_drawdown(portfolio_returns),
            "Downside Deviation": downside_deviation(
                portfolio_returns,
                periods_per_year=periods_per_year,
            ),
            "Sortino Ratio": sortino_ratio(
                portfolio_returns,
                periods_per_year=periods_per_year,
            ),
            "Calmar Ratio": calmar_ratio(
                portfolio_returns,
                periods_per_year=periods_per_year,
            ),
            "VaR (95%)": value_at_risk(portfolio_returns),
            "CVaR (95%)": conditional_value_at_risk(portfolio_returns),
        },

        "Statistics": {
            "Mean Daily Return": mean_return(portfolio_returns),
            "Median Daily Return": median_return(portfolio_returns),
            "Best Day": best_day(portfolio_returns),
            "Worst Day": worst_day(portfolio_returns),
            "Positive Days": positive_days(portfolio_returns),
            "Negative Days": negative_days(portfolio_returns),
            "Win Rate": win_rate(portfolio_returns),
        },

        "Distribution": {
            "Standard Deviation": standard_deviation(portfolio_returns),
            "Skewness": skewness(portfolio_returns),
            "Kurtosis": kurtosis(portfolio_returns),
            "5th Percentile": percentile(portfolio_returns, 5),
            "25th Percentile": percentile(portfolio_returns, 25),
            "75th Percentile": percentile(portfolio_returns, 75),
            "95th Percentile": percentile(portfolio_returns, 95),
            "Interquartile Range": interquartile_range(portfolio_returns),
        },
    }

    # ------------------------------------------------------
    # Benchmark Analysis
    # ------------------------------------------------------

    if benchmark_returns is not None:

        report["Benchmark Analysis"] = {

            "Correlation": correlation(
                portfolio_returns,
                benchmark_returns,
            ),

            "Beta": beta(
                portfolio_returns,
                benchmark_returns,
            ),

            "Alpha": alpha(
                portfolio_returns,
                benchmark_returns,
                periods_per_year=periods_per_year,
            ),

            "Tracking Error": tracking_error(
                portfolio_returns,
                benchmark_returns,
                periods_per_year=periods_per_year,
            ),

            "Active Return": active_return(
                portfolio_returns,
                benchmark_returns,
                periods_per_year=periods_per_year,
            ),

            "Information Ratio": information_ratio(
                portfolio_returns,
                benchmark_returns,
                periods_per_year=periods_per_year,
            ),
        }

    # ------------------------------------------------------
    # Factor Analysis
    # ------------------------------------------------------

    if factor_data is not None:

        factor_results = factor_analysis(
            portfolio_returns,
            factor_data,
        )

        if factor_results:
            report["Factor Analysis"] = factor_results

    return report


def print_report(report: dict) -> None:
    """
    Print a structured report.
    """

    percentage_metrics = {
        "Total Return",
        "Annualized Return",
        "Annualized Volatility",
        "Maximum Drawdown",
        "Mean Daily Return",
        "Median Daily Return",
        "Best Day",
        "Worst Day",
        "Win Rate",
        "Standard Deviation",
        "5th Percentile",
        "25th Percentile",
        "75th Percentile",
        "95th Percentile",
        "Interquartile Range",
        "Downside Deviation",
        "VaR (95%)",
        "CVaR (95%)",
        "Alpha",
        "Tracking Error",
        "Active Return",
    }

    integer_metrics = {
        "Positive Days",
        "Negative Days",
    }

    print("=" * 70)
    print("                    AlphaLens Strategy Report")
    print("=" * 70)

    for section, metrics in report.items():

        print(f"\n{section}")
        print("-" * 70)

        # Handle nested sections (Factor Analysis)
        if any(isinstance(v, dict) for v in metrics.values()):

            for model, model_metrics in metrics.items():

                print(f"\n{model}")

                for metric, value in model_metrics.items():

                    if isinstance(value, (int, float)):

                        if metric in percentage_metrics:
                            print(f"  {metric:<33}: {value:.2%}")

                        else:
                            print(f"  {metric:<33}: {value:.4f}")

                    else:
                        print(f"  {metric:<33}: {value}")

            continue

        for metric, value in metrics.items():

            if metric in percentage_metrics:
                print(f"{metric:<35}: {value:.2%}")

            elif metric in integer_metrics:
                print(f"{metric:<35}: {value}")

            else:
                print(f"{metric:<35}: {value:.4f}")

    print("\n" + "=" * 70)