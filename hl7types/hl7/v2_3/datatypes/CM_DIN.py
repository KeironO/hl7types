"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_DIN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .TS import TS


class CM_DIN(BaseModel):
    """HL7 v2 CM_DIN data type.

    Attributes
    ----------
    cm_din_1 : TS | None
        CM_DIN.1 (opt) - date (TS)

    cm_din_2 : CE | None
        CM_DIN.2 (opt) - institution name (CE)
    """

    cm_din_1: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_din_1",
            "date",
            "CM_DIN.1",
        ),
        serialization_alias="CM_DIN.1",
        title="date",
    )

    cm_din_2: Optional[CE] = Field(
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
