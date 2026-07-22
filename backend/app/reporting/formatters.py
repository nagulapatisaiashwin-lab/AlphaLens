"""
Formatting utilities for AlphaLens reporting.
"""

from __future__ import annotations

from typing import Any


def format_percent(value: Any, decimals: int = 2) -> str:
    """Format a decimal value as a percentage."""

    if value is None:
        return "N/A"

    try:
        return f"{value * 100:.{decimals}f}%"
    except (TypeError, ValueError):
        return "N/A"


def format_percentage(value: Any, decimals: int = 2) -> str:
    """Format an already-percentage value."""

    if value is None:
        return "N/A"

    try:
        return f"{value:.{decimals}f}%"
    except (TypeError, ValueError):
        return "N/A"


def format_currency(value: Any, symbol: str = "₹", decimals: int = 2) -> str:
    """Format a currency value."""

    if value is None:
        return "N/A"

    try:
        return f"{symbol}{value:,.{decimals}f}"
    except (TypeError, ValueError):
        return "N/A"


def format_number(value: Any, decimals: int = 2) -> str:
    """Format a floating-point number."""

    if value is None:
        return "N/A"

    try:
        return f"{value:,.{decimals}f}"
    except (TypeError, ValueError):
        return "N/A"


def format_integer(value: Any) -> str:
    """Format an integer."""

    if value is None:
        return "N/A"

    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return "N/A"


def format_ratio(value: Any, decimals: int = 2) -> str:
    """Format ratios such as Sharpe or Sortino."""

    if value is None:
        return "N/A"

    try:
        return f"{value:.{decimals}f}"
    except (TypeError, ValueError):
        return "N/A"


def format_metric(metric: str, value: Any) -> str:
    """
    Automatically format a metric based on its name.
    """

    metric = metric.lower()

    if any(x in metric for x in [
        "return",
        "cagr",
        "drawdown",
        "volatility",
    ]):
        return format_percent(value)

    if any(x in metric for x in [
        "sharpe",
        "sortino",
        "calmar",
        "information",
        "beta",
        "alpha",
    ]):
        return format_ratio(value)

    if any(x in metric for x in [
        "capital",
        "value",
        "equity",
        "cash",
    ]):
        return format_currency(value)

    if isinstance(value, int):
        return format_integer(value)

    if isinstance(value, float):
        return format_number(value)

    return str(value)