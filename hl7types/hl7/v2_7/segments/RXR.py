"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RXR
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class RXR(HL7Model):
    """Pharmacy/Treatment Route (S4.A.4.1).

    Attributes
    ----------
    rxr_1 : CWE
        RXR.1 - Route (CWE) R S4.A.4.1.1 | 0162 - Route of Administration

    rxr_2 : CWE | None
        RXR.2 - Administration Site (CWE) O S4.A.4.1.2 | 0550 - Body Parts

    rxr_3 : CWE | None
        RXR.3 - Administration Device (CWE) O S4.A.4.1.3 | 0164 - Administration Device

    rxr_4 : CWE | None
        RXR.4 - Administration Method (CWE) O S4.A.4.1.4 | 0165 - Administration Method

    rxr_5 : CWE | None
        RXR.5 - Routing Instruction (CWE) O S4.A.4.1.5 | 9999 - no table for CE

    rxr_6 : CWE | None
        RXR.6 - Administration Site Modifier (CWE) O S4.A.4.1.6 | 0495 - Body Site Modifier
    """

    rxr_1: CWE = Field(
        validation_alias=AliasChoices(
            "rxr_1",
            "route",
            "RXR.1",
        ),
        serialization_alias="RXR.1",
        title="Route",
        description="R | Item #00309 | Table 0162 - Route of Administration",
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
        description="O | Item #00310 | Table 0550 - Body Parts",
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
        description="O | Item #00311 | Table 0164 - Administration Device",
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
        description="O | Item #00312 | Table 0165 - Administration Method",
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
        description="O | Item #01315 | Table 9999 - no table for CE",
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
        description="O | Item #01670 | Table 0495 - Body Site Modifier",
    )

    model_config = ConfigDict(populate_by_name=True)
