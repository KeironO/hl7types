"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SCV
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class SCV(BaseModel):
    """HL7 v2 SCV data type."""

    scv_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "scv_1",
            "parameter_class",
            "SCV.1",
        ),
        serialization_alias="SCV.1",
        title="parameter class",
    )

    scv_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "scv_2",
            "parameter_value",
            "SCV.2",
        ),
        serialization_alias="SCV.2",
        title="parameter value",
    )

    model_config = {"populate_by_name": True}
