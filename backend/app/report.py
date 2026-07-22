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


def analyze_strategy(returns: pd.Series) -> dict:
    """
    Generate a structured strategy report.
    """

    return {

        "Performance": {
            "Total Return": total_return(returns),
            "Annualized Return": annualized_return(returns),
            "Sharpe Ratio": sharpe_ratio(returns),
        },

        "Risk": {
    "Annualized Volatility": volatility(returns),
    "Maximum Drawdown": max_drawdown(returns),
    "Downside Deviation": downside_deviation(returns),
    "Sortino Ratio": sortino_ratio(returns),
    "Calmar Ratio": calmar_ratio(returns),
    "VaR (95%)": value_at_risk(returns),
    "CVaR (95%)": conditional_value_at_risk(returns),
},

        "Statistics": {
            "Mean Daily Return": mean_return(returns),
            "Median Daily Return": median_return(returns),
            "Best Day": best_day(returns),
            "Worst Day": worst_day(returns),
            "Positive Days": positive_days(returns),
            "Negative Days": negative_days(returns),
            "Win Rate": win_rate(returns),
        },

        "Distribution": {
            "Standard Deviation": standard_deviation(returns),
            "Skewness": skewness(returns),
            "Kurtosis": kurtosis(returns),
            "5th Percentile": percentile(returns, 5),
            "25th Percentile": percentile(returns, 25),
            "75th Percentile": percentile(returns, 75),
            "95th Percentile": percentile(returns, 95),
            "Interquartile Range": interquartile_range(returns),
        }
    }


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

        for metric, value in metrics.items():

            if metric in percentage_metrics:
                print(f"{metric:<35}: {value:.2%}")

            elif metric in integer_metrics:
                print(f"{metric:<35}: {value}")

            else:
                print(f"{metric:<35}: {value:.4f}")

    print("\n" + "=" * 70)