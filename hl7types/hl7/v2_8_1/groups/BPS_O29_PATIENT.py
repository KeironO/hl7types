"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BPS_O29.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

from .BPS_O29_PATIENT_VISIT import BPS_O29_PATIENT_VISIT

_ARV = ARV
_BPS_O29_PATIENT_VISIT = BPS_O29_PATIENT_VISIT
_NTE = NTE
_PD1 = PD1
_PID = PID
_PRT = PRT


class BPS_O29_PATIENT(BaseModel):
    """HL7 v2 BPS_O29.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT_VISIT (Optional[BPS_O29_PATIENT_VISIT]): optional
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT_VISIT: Optional[_BPS_O29_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
