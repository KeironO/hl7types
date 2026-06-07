"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PGL_PC6
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
    """HL7 v2 PGL_PC6 message.

    Attributes:
        MSH (MSH): required
        PID (PID): required
        PATIENT_VISIT (Optional[PGL_PC6_PATIENT_VISIT]): optional
        GOAL (List[PGL_PC6_GOAL]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: Optional[_PGL_PC6_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    GOAL: List[_PGL_PC6_GOAL] = Field(
        min_length=1,
        title="GOAL",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
