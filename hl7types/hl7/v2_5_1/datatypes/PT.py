"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PT
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class PT(BaseModel):
    """HL7 v2 PT data type."""

    pt_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pt_1",
            "processing_id",
            "PT.1",
        ),
        serialization_alias="PT.1",
        title="Processing ID",
    )

    pt_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pt_2",
            "processing_mode",
            "PT.2",
        ),
        serialization_alias="PT.2",
        title="Processing Mode",
    )

    model_config = {"populate_by_name": True}
