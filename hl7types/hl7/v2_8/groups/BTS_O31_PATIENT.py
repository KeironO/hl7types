"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
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
from ..segments.PRT import PRT

from .BTS_O31_PATIENT_VISIT import BTS_O31_PATIENT_VISIT

_BTS_O31_PATIENT_VISIT = BTS_O31_PATIENT_VISIT
_NTE = NTE
_PD1 = PD1
_PID = PID
_PRT = PRT


class BTS_O31_PATIENT(HL7Model):
    """HL7 v2 BTS_O31.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT_VISIT (Optional[BTS_O31_PATIENT_VISIT]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Additional Demographic",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT_VISIT: Optional[_BTS_O31_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    model_config = {"populate_by_name": True}
