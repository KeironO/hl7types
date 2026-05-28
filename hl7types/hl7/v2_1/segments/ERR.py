"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ERR
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class ERR(BaseModel):
    """HL7 v2 ERR segment."""

    err_1: list[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "err_1",
            "error_code_and_location",
            "ERR.1",
        ),
        serialization_alias="ERR.1",
        title="ERROR CODE AND LOCATION",
        description="Item #80 | Table HL70060",
    )

    model_config = {"populate_by_name": True}
