"""
Core result objects used throughout AlphaLens.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from app.io.frequency import FrequencyInfo


@dataclass
class AnalysisResult:
    """
    Stores everything generated during one analysis run.
    """

    dataset_type: str

    frequency: FrequencyInfo

    data: pd.DataFrame

    returns: pd.Series

    metrics: dict

    charts: dict[str, Path] = field(default_factory=dict)

    metadata: dict = field(default_factory=dict)