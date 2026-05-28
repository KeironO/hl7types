"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PRR_PC5.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PID import PID

from .PRR_PC5_PATIENT_VISIT import PRR_PC5_PATIENT_VISIT
from .PRR_PC5_PROBLEM import PRR_PC5_PROBLEM

_PID = PID
_PRR_PC5_PATIENT_VISIT = PRR_PC5_PATIENT_VISIT
_PRR_PC5_PROBLEM = PRR_PC5_PROBLEM


class PRR_PC5_PATIENT(BaseModel):
    """HL7 v2 PRR_PC5.PATIENT group.

    Attributes:
        PID (PID): required
        PATIENT_VISIT (Optional[PRR_PC5_PATIENT_VISIT]): optional
        PROBLEM (List[PRR_PC5_PROBLEM]): required
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: Optional[_PRR_PC5_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    PROBLEM: List[_PRR_PC5_PROBLEM] = Field(
        default=...,
        title="PROBLEM",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
