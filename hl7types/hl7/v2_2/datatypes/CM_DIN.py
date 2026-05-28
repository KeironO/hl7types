"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_DIN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .TS import TS


class CM_DIN(BaseModel):
    """HL7 v2 CM_DIN data type."""

    cm_din_1: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_din_1",
            "date",
            "CM_DIN.1",
        ),
        serialization_alias="CM_DIN.1",
        title="Date",
    )

    cm_din_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_din_2",
            "institution_name",
            "CM_DIN.2",
        ),
        serialization_alias="CM_DIN.2",
        title="institution name",
    )

    model_config = {"populate_by_name": True}
