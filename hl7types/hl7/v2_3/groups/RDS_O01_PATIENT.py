"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RDS_O01.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from .RDS_O01_PATIENT_VISIT import RDS_O01_PATIENT_VISIT

_AL1 = AL1
_NTE = NTE
_PD1 = PD1
_PID = PID
_RDS_O01_PATIENT_VISIT = RDS_O01_PATIENT_VISIT


class RDS_O01_PATIENT(BaseModel):
    """HL7 v2 RDS_O01.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        AL1 (Optional[List[AL1]]): optional
        PATIENT_VISIT (Optional[RDS_O01_PATIENT_VISIT]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: _PD1 | None = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    AL1: list[_AL1] | None = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    PATIENT_VISIT: _RDS_O01_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
