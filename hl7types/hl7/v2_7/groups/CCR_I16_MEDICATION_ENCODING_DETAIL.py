"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.MEDICATION_ENCODING_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

_OBX = OBX
_RXC = RXC
_RXE = RXE
_RXR = RXR


class CCR_I16_MEDICATION_ENCODING_DETAIL(HL7Model):
    """HL7 v2 CCR_I16.MEDICATION_ENCODING_DETAIL group.

    Attributes:
        RXE (RXE): Pharmacy/Treatment Encoded Order, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy/Treatment Encoded Order",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Pharmacy/Treatment Component Order",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = {"populate_by_name": True}
