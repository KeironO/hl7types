"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class RI(BaseModel):
    """HL7 v2 RI data type."""

    ri_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ri_1",
            "repeat_pattern",
            "RI.1",
        ),
        serialization_alias="RI.1",
        title="repeat pattern",
    )

    ri_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ri_2",
            "explicit_time_interval",
            "RI.2",
        ),
        serialization_alias="RI.2",
        title="explicit time interval",
    )

    model_config = {"populate_by_name": True}
