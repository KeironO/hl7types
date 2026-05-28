"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PGL_PC6
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.PGL_PC6_GOAL import PGL_PC6_GOAL
from ..groups.PGL_PC6_PATIENT_VISIT import PGL_PC6_PATIENT_VISIT
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

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

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: _PGL_PC6_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    GOAL: list[_PGL_PC6_GOAL] = Field(
        default=...,
        title="GOAL",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
