"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_CCD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class CM_CCD(BaseModel):
    """HL7 v2 CM_CCD data type."""

    cm_ccd_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ccd_1",
            "when_to_charge",
            "CM_CCD.1",
        ),
        serialization_alias="CM_CCD.1",
        title="When to Charge",
    )

    cm_ccd_2: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ccd_2",
            "date_time",
            "CM_CCD.2",
        ),
        serialization_alias="CM_CCD.2",
        title="date/time",
    )

    model_config = {"populate_by_name": True}
