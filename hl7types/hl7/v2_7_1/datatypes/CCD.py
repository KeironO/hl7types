"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CCD(BaseModel):
    """HL7 v2 CCD data type."""

    ccd_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ccd_1",
            "invocation_event",
            "CCD.1",
        ),
        serialization_alias="CCD.1",
        title="Invocation Event",
    )

    ccd_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccd_2",
            "date_time",
            "CCD.2",
        ),
        serialization_alias="CCD.2",
        title="Date/time",
    )

    model_config = {"populate_by_name": True}
