"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCM_I21.MEDICATION_ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR
from .CCM_I21_MEDICATION_ORDER_OBSERVATION import CCM_I21_MEDICATION_ORDER_OBSERVATION

_CCM_I21_MEDICATION_ORDER_OBSERVATION = CCM_I21_MEDICATION_ORDER_OBSERVATION
_RXC = RXC
_RXO = RXO
_RXR = RXR


class CCM_I21_MEDICATION_ORDER_DETAIL(BaseModel):
    """HL7 v2 CCM_I21.MEDICATION_ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        MEDICATION_ORDER_OBSERVATION (Optional[List[CCM_I21_MEDICATION_ORDER_OBSERVATION]]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    RXR: list[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: list[_RXC] | None = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    MEDICATION_ORDER_OBSERVATION: list[_CCM_I21_MEDICATION_ORDER_OBSERVATION] | None = Field(
        default=None,
        title="MEDICATION_ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
