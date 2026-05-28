"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RI
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE


class RI(BaseModel):
    """HL7 v2 RI data type."""

    ri_1: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ri_1",
            "repeat_pattern",
            "RI.1",
        ),
        serialization_alias="RI.1",
        title="Repeat Pattern",
    )

    ri_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ri_2",
            "explicit_time_interval",
            "RI.2",
        ),
        serialization_alias="RI.2",
        title="Explicit Time Interval",
    )

    model_config = {"populate_by_name": True}
