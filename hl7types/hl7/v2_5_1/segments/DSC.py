"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: DSC
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class DSC(BaseModel):
    """HL7 v2 DSC segment."""

    dsc_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsc_1",
            "continuation_pointer",
            "DSC.1",
        ),
        serialization_alias="DSC.1",
        title="Continuation Pointer",
        description="Item #14",
    )

    dsc_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsc_2",
            "continuation_style",
            "DSC.2",
        ),
        serialization_alias="DSC.2",
        title="Continuation Style",
        description="Item #1354 | Table HL70398",
    )

    model_config = {"populate_by_name": True}
