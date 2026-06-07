"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RXR
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class RXR(HL7Model):
    """HL7 v2 RXR segment.

    Attributes
    ----------
    rxr_1 : CE
        RXR.1 (req) - Route (CE)

    rxr_2 : CE | None
        RXR.2 (opt) - Site (CE)

    rxr_3 : CE | None
        RXR.3 (opt) - Administration Device (CE)

    rxr_4 : CE | None
        RXR.4 (opt) - Administration Method (CE)

    rxr_5 : CE | None
        RXR.5 (opt) - Routing Instruction (CE)
    """

    rxr_1: CE = Field(
        validation_alias=AliasChoices(
            "rxr_1",
            "route",
            "RXR.1",
        ),
        serialization_alias="RXR.1",
        title="Route",
        description="Item #309 | Table HL70162",
    )

    rxr_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxr_2",
            "site",
            "RXR.2",
        ),
        serialization_alias="RXR.2",
        title="Site",
        description="Item #310 | Table HL70163",
    )

    rxr_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxr_3",
            "administration_device",
            "RXR.3",
        ),
        serialization_alias="RXR.3",
        title="Administration Device",
        description="Item #311 | Table HL70164",
    )

    rxr_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxr_4",
            "administration_method",
            "RXR.4",
        ),
        serialization_alias="RXR.4",
        title="Administration Method",
        description="Item #312 | Table HL70165",
    )

    rxr_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxr_5",
            "routing_instruction",
            "RXR.5",
        ),
        serialization_alias="RXR.5",
        title="Routing Instruction",
        description="Item #1315",
    )

    model_config = {"populate_by_name": True}
