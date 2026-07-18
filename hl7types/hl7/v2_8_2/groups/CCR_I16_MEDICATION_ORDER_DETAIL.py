"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCR_I16.MEDICATION_ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .CCR_I16_MEDICATION_ORDER_OBSERVATION import CCR_I16_MEDICATION_ORDER_OBSERVATION

_CCR_I16_MEDICATION_ORDER_OBSERVATION = CCR_I16_MEDICATION_ORDER_OBSERVATION
_RXC = RXC
_RXO = RXO
_RXR = RXR


class CCR_I16_MEDICATION_ORDER_DETAIL(HL7Model):
    """HL7 v2 CCR_I16.MEDICATION_ORDER_DETAIL group.

    Attributes:
        RXO (RXO): Pharmacy/Treatment Order, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
        MEDICATION_ORDER_OBSERVATION (Optional[List[CCR_I16_MEDICATION_ORDER_OBSERVATION]]): optional
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

    MEDICATION_ORDER_OBSERVATION: Optional[List[_CCR_I16_MEDICATION_ORDER_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ORDER_OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
