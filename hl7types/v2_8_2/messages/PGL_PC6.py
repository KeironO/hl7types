"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PGL_PC6
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.PGL_PC6_GOAL import PGL_PC6_GOAL
from ..groups.PGL_PC6_PATIENT_VISIT import PGL_PC6_PATIENT_VISIT

_MSH = MSH
_PGL_PC6_GOAL = PGL_PC6_GOAL
_PGL_PC6_PATIENT_VISIT = PGL_PC6_PATIENT_VISIT
_PID = PID
_SFT = SFT
_UAC = UAC


class PGL_PC6(BaseModel):
    """HL7 v2 PGL_PC6 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        PID (PID): required
        PATIENT_VISIT (Optional[PGL_PC6_PATIENT_VISIT]): optional
        GOAL (List[PGL_PC6_GOAL]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: Optional[_PGL_PC6_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    GOAL: List[_PGL_PC6_GOAL] = Field(
        default=...,
        title="GOAL",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
