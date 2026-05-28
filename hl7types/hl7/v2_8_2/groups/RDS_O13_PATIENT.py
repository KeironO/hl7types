"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RDS_O13.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from ..segments.NTE import NTE
from ..segments.PID import PID

from .RDS_O13_ADDITIONAL_DEMOGRAPHICS import RDS_O13_ADDITIONAL_DEMOGRAPHICS
from .RDS_O13_PATIENT_VISIT import RDS_O13_PATIENT_VISIT

_AL1 = AL1
_NTE = NTE
_PID = PID
_RDS_O13_ADDITIONAL_DEMOGRAPHICS = RDS_O13_ADDITIONAL_DEMOGRAPHICS
_RDS_O13_PATIENT_VISIT = RDS_O13_PATIENT_VISIT


class RDS_O13_PATIENT(BaseModel):
    """HL7 v2 RDS_O13.PATIENT group.

    Attributes:
        PID (PID): required
        ADDITIONAL_DEMOGRAPHICS (Optional[RDS_O13_ADDITIONAL_DEMOGRAPHICS]): optional
        NTE (Optional[List[NTE]]): optional
        AL1 (Optional[List[AL1]]): optional
        PATIENT_VISIT (Optional[RDS_O13_PATIENT_VISIT]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    ADDITIONAL_DEMOGRAPHICS: Optional[_RDS_O13_ADDITIONAL_DEMOGRAPHICS] = Field(
        default=None,
        title="ADDITIONAL_DEMOGRAPHICS",
        description="Optional",
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

    PATIENT_VISIT: Optional[_RDS_O13_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
