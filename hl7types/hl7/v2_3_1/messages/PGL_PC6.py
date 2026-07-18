"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PGL_PC6
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.PID import PID

from ..groups.PGL_PC6_GOAL import PGL_PC6_GOAL
from ..groups.PGL_PC6_PATIENT_VISIT import PGL_PC6_PATIENT_VISIT

_MSH = MSH
_PGL_PC6_GOAL = PGL_PC6_GOAL
_PGL_PC6_PATIENT_VISIT = PGL_PC6_PATIENT_VISIT
_PID = PID


class PGL_PC6(HL7Model):
    """PGL - PC/ Goal Add.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        PID (PID): PID - patient identification segment, required
        PATIENT_VISIT (Optional[PGL_PC6_PATIENT_VISIT]): optional
        GOAL (List[PGL_PC6_GOAL]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
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
