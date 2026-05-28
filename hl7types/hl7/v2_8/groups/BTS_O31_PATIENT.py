"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: BTS_O31.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT
from .BTS_O31_PATIENT_VISIT import BTS_O31_PATIENT_VISIT

_BTS_O31_PATIENT_VISIT = BTS_O31_PATIENT_VISIT
_NTE = NTE
_PD1 = PD1
_PID = PID
_PRT = PRT


class BTS_O31_PATIENT(BaseModel):
    """HL7 v2 BTS_O31.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT_VISIT (Optional[BTS_O31_PATIENT_VISIT]): optional
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

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT_VISIT: _BTS_O31_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
