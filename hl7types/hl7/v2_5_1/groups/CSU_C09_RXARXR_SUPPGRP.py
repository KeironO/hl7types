"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: CSU_C09.RXARXR_SUPPGRP
Type: Group
"""
from __future__ import annotations

from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXR import RXR

_RXA = RXA
_RXR = RXR


class CSU_C09_RXARXR_SUPPGRP(HL7Model):
    """HL7 v2 CSU_C09.RXARXR_SUPPGRP group.

    Attributes:
        RXA (RXA): Pharmacy/Treatment Administration, required
        RXR (RXR): Pharmacy/Treatment Route, required
    """

    RXA: _RXA = Field(
        title="RXA",
        description="Pharmacy/Treatment Administration",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    model_config = {"populate_by_name": True}
