"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: BTS_O31.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .BTS_O31_PATIENT_VISIT import BTS_O31_PATIENT_VISIT

_BTS_O31_PATIENT_VISIT = BTS_O31_PATIENT_VISIT
_NTE = NTE
_PD1 = PD1
_PID = PID


class BTS_O31_PATIENT(HL7Model):
    """HL7 v2 BTS_O31.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT_VISIT (Optional[BTS_O31_PATIENT_VISIT]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT_VISIT: Optional[_BTS_O31_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
