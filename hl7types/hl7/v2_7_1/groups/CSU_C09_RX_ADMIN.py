"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CSU_C09.RX_ADMIN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PRT import PRT
from ..segments.RXA import RXA
from ..segments.RXR import RXR

_PRT = PRT
_RXA = RXA
_RXR = RXR


class CSU_C09_RX_ADMIN(HL7Model):
    """HL7 v2 CSU_C09.RX_ADMIN group.

    Attributes:
        RXA (RXA): Pharmacy/Treatment Administration, required
        RXR (RXR): Pharmacy/Treatment Route, required
        PRT (Optional[List[PRT]]): Participation Information, optional
    """

    RXA: _RXA = Field(
        title="RXA",
        description="Pharmacy/Treatment Administration",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    model_config = ConfigDict(populate_by_name=True)
