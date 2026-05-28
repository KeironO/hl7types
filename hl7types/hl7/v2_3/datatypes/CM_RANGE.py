"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_RANGE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CE import CE


class CM_RANGE(BaseModel):
    """HL7 v2 CM_RANGE data type."""

    cm_range_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_range_1",
            "low_value",
            "CM_RANGE.1",
        ),
        serialization_alias="CM_RANGE.1",
        title="Low Value",
    )

    cm_range_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_range_2",
            "high_value",
            "CM_RANGE.2",
        ),
        serialization_alias="CM_RANGE.2",
        title="High Value",
    )

    model_config = {"populate_by_name": True}
