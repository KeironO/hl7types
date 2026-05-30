"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CQU_I19.MEDICATION_ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .CQU_I19_MEDICATION_ORDER_OBSERVATION import CQU_I19_MEDICATION_ORDER_OBSERVATION

_CQU_I19_MEDICATION_ORDER_OBSERVATION = CQU_I19_MEDICATION_ORDER_OBSERVATION
_RXC = RXC
_RXO = RXO
_RXR = RXR


class CQU_I19_MEDICATION_ORDER_DETAIL(HL7Model):
    """HL7 v2 CQU_I19.MEDICATION_ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        MEDICATION_ORDER_OBSERVATION (Optional[List[CQU_I19_MEDICATION_ORDER_OBSERVATION]]): optional
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

    MEDICATION_ORDER_OBSERVATION: Optional[List[_CQU_I19_MEDICATION_ORDER_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
