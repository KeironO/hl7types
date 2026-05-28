"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCR_I16.MEDICATION_ORDER_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .CCR_I16_MEDICATION_ORDER_OBSERVATION import CCR_I16_MEDICATION_ORDER_OBSERVATION

_CCR_I16_MEDICATION_ORDER_OBSERVATION = CCR_I16_MEDICATION_ORDER_OBSERVATION
_RXC = RXC
_RXO = RXO
_RXR = RXR


class CCR_I16_MEDICATION_ORDER_DETAIL(BaseModel):
    """HL7 v2 CCR_I16.MEDICATION_ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        MEDICATION_ORDER_OBSERVATION (Optional[List[CCR_I16_MEDICATION_ORDER_OBSERVATION]]): optional
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

    MEDICATION_ORDER_OBSERVATION: Optional[List[_CCR_I16_MEDICATION_ORDER_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
