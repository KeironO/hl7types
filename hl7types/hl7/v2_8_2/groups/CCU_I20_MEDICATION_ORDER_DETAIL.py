"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCU_I20.MEDICATION_ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .CCU_I20_MEDICATION_ORDER_OBSERVATION import CCU_I20_MEDICATION_ORDER_OBSERVATION

_CCU_I20_MEDICATION_ORDER_OBSERVATION = CCU_I20_MEDICATION_ORDER_OBSERVATION
_RXC = RXC
_RXO = RXO
_RXR = RXR


class CCU_I20_MEDICATION_ORDER_DETAIL(HL7Model):
    """HL7 v2 CCU_I20.MEDICATION_ORDER_DETAIL group.

    Attributes:
        RXO (RXO): Pharmacy/Treatment Order, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
        MEDICATION_ORDER_OBSERVATION (Optional[List[CCU_I20_MEDICATION_ORDER_OBSERVATION]]): optional
    """

    RXO: _RXO = Field(
        title="RXO",
        description="Pharmacy/Treatment Order",
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

    MEDICATION_ORDER_OBSERVATION: Optional[List[_CCU_I20_MEDICATION_ORDER_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ORDER_OBSERVATION",
    )

    model_config = {"populate_by_name": True}
