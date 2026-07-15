"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RXR
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class RXR(HL7Model):
    """Pharmacy route segment (S4.8.3).

    Attributes
    ----------
    rxr_1 : CE
        RXR.1 - Route (CE) R S4.8.3.1 | 0162 - Route of Administration

    rxr_2 : CE | None
        RXR.2 - Site (CE) O S4.8.3.2 | 0163 - Administrative Site

    rxr_3 : CE | None
        RXR.3 - Administration Device (CE) O S4.8.3.3 | 0164 - Adminstration Device

    rxr_4 : CE | None
        RXR.4 - Administration Method (CE) O S4.8.3.4 | 0165 - Administration Method
    """

    rxr_1: CE = Field(
        validation_alias=AliasChoices(
            "rxr_1",
            "route",
            "RXR.1",
        ),
        serialization_alias="RXR.1",
        title="Route",
        description="R | Item #00309 | Table 0162 - Route of Administration",
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
        description="O | Item #00310 | Table 0163 - Administrative Site",
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
        description="O | Item #00311 | Table 0164 - Adminstration Device",
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
        description="O | Item #00312 | Table 0165 - Administration Method",
    )

    model_config = {"populate_by_name": True}
