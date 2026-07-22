"""
Pydantic response models for the AlphaLens API.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class AnalysisResponse(BaseModel):
    """
    Response returned by the analysis endpoint.
    """

    dataset_type: str
    frequency: str
    observations: int

    metrics: dict[str, Any] = Field(default_factory=dict)

    charts: dict[str, Any] = Field(default_factory=dict)

    metadata: dict[str, Any] = Field(default_factory=dict)