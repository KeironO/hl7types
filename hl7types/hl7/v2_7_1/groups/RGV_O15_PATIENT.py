"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RGV_O15.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from ..segments.NTE import NTE
from ..segments.PID import PID

from .RGV_O15_PATIENT_VISIT import RGV_O15_PATIENT_VISIT

_AL1 = AL1
_NTE = NTE
_PID = PID
_RGV_O15_PATIENT_VISIT = RGV_O15_PATIENT_VISIT


class RGV_O15_PATIENT(BaseModel):
    """HL7 v2 RGV_O15.PATIENT group.

    Attributes:
        PID (PID): required
        NTE (Optional[List[NTE]]): optional
        AL1 (Optional[List[AL1]]): optional
        PATIENT_VISIT (Optional[RGV_O15_PATIENT_VISIT]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    PATIENT_VISIT: Optional[_RGV_O15_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
