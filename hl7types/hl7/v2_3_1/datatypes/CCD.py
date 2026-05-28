"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CCD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class CCD(BaseModel):
    """HL7 v2 CCD data type."""

    ccd_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccd_1",
            "when_to_charge_code",
            "CCD.1",
        ),
        serialization_alias="CCD.1",
        title="when to charge code",
    )

    ccd_2: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ccd_2",
            "date_time",
            "CCD.2",
        ),
        serialization_alias="CCD.2",
        title="date/time",
    )

    model_config = {"populate_by_name": True}
