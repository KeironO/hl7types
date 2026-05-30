"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCR_I16.MEDICATION_ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

_OBX = OBX
_RXC = RXC
_RXO = RXO
_RXR = RXR


class CCR_I16_MEDICATION_ORDER_DETAIL(HL7Model):
    """HL7 v2 CCR_I16.MEDICATION_ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBX (Optional[List[OBX]]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
