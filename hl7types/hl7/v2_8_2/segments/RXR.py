"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RXR
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class RXR(HL7Model):
    """Pharmacy/Treatment Route (S4.A.2).

    Attributes
    ----------
    rxr_1 : CWE
        RXR.1 (req) - Route (CWE) S4.A.2.1 | 0162 - Route of Administration

    rxr_2 : CWE | None
        RXR.2 (opt) - Administration Site (CWE) S4.A.2.2 | 0550 - Body Parts

    rxr_3 : CWE | None
        RXR.3 (opt) - Administration Device (CWE) S4.A.2.3 | 0164 - Administration Device

    rxr_4 : CWE | None
        RXR.4 (opt) - Administration Method (CWE) S4.A.2.4 | 0165 - Administration Method

    rxr_5 : CWE | None
        RXR.5 (opt) - Routing Instruction (CWE) S4.A.2.5 | 9999 - no table for CE

    rxr_6 : CWE | None
        RXR.6 (opt) - Administration Site Modifier (CWE) S4.A.2.6 | 0495 - Body Site Modifier
    """

    rxr_1: CWE = Field(
        validation_alias=AliasChoices(
            "rxr_1",
            "route",
            "RXR.1",
        ),
        serialization_alias="RXR.1",
        title="Route",
        description="Item #309 | Table HL70162",
    )

    rxr_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxr_2",
            "administration_site",
            "RXR.2",
        ),
        serialization_alias="RXR.2",
        title="Administration Site",
        description="Item #310 | Table HL70550",
    )

    rxr_3: Optional[CWE] = Field(
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

    rxr_4: Optional[CWE] = Field(
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

    rxr_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxr_5",
            "routing_instruction",
            "RXR.5",
        ),
        serialization_alias="RXR.5",
        title="Routing Instruction",
        description="Item #1315 | Table HL79999",
    )

    rxr_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxr_6",
            "administration_site_modifier",
            "RXR.6",
        ),
        serialization_alias="RXR.6",
        title="Administration Site Modifier",
        description="Item #1670 | Table HL70495",
    )

    model_config = {"populate_by_name": True}
