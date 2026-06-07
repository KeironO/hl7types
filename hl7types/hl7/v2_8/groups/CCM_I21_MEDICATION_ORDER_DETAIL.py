"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCM_I21.MEDICATION_ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .CCM_I21_MEDICATION_ORDER_OBSERVATION import CCM_I21_MEDICATION_ORDER_OBSERVATION

_CCM_I21_MEDICATION_ORDER_OBSERVATION = CCM_I21_MEDICATION_ORDER_OBSERVATION
_RXC = RXC
_RXO = RXO
_RXR = RXR


class CCM_I21_MEDICATION_ORDER_DETAIL(HL7Model):
    """HL7 v2 CCM_I21.MEDICATION_ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        MEDICATION_ORDER_OBSERVATION (Optional[List[CCM_I21_MEDICATION_ORDER_OBSERVATION]]): optional
    """

    RXO: _RXO = Field(
        title="RXO",
        description="Required",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    MEDICATION_ORDER_OBSERVATION: Optional[List[_CCM_I21_MEDICATION_ORDER_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
