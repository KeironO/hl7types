"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: DIN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CE import CE
from .TS import TS


class DIN(HL7Model):
    """HL7 v2 DIN data type.

    Attributes
    ----------
    din_1 : TS | None
        DIN.1 (opt) - Date (TS)

    din_2 : CE | None
        DIN.2 (opt) - Institution Name (CE)
    """

    din_1: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "din_1",
            "date",
            "DIN.1",
        ),
        serialization_alias="DIN.1",
        title="Date",
    )

    din_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "din_2",
            "institution_name",
            "DIN.2",
        ),
        serialization_alias="DIN.2",
        title="Institution Name",
    )

    model_config = {"populate_by_name": True}
