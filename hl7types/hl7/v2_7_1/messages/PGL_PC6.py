"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PGL_PC6
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class PGL_PC6(HL7Model):
    """PGL - PC/ goal add (S12.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PID (PID): Patient Identification, required
        PATIENT_VISIT (Optional[PGL_PC6_PATIENT_VISIT]): optional
        GOAL (List[PGL_PC6_GOAL]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PATIENT_VISIT: Optional[_PGL_PC6_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    GOAL: List[_PGL_PC6_GOAL] = Field(
        min_length=1,
        title="GOAL",
    )

    model_config = ConfigDict(populate_by_name=True)
