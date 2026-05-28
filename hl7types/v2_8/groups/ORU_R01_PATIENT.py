"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORU_R01.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

from .ORU_R01_PATIENT_OBSERVATION import ORU_R01_PATIENT_OBSERVATION
from .ORU_R01_VISIT import ORU_R01_VISIT

_ARV = ARV
_NK1 = NK1
_NTE = NTE
_ORU_R01_PATIENT_OBSERVATION = ORU_R01_PATIENT_OBSERVATION
_ORU_R01_VISIT = ORU_R01_VISIT
_PD1 = PD1
_PID = PID
_PRT = PRT


class ORU_R01_PATIENT(BaseModel):
    """HL7 v2 ORU_R01.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        NK1 (Optional[List[NK1]]): optional
        ARV (Optional[List[ARV]]): optional
        PATIENT_OBSERVATION (Optional[List[ORU_R01_PATIENT_OBSERVATION]]): optional
        VISIT (Optional[ORU_R01_VISIT]): optional
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    PATIENT_OBSERVATION: Optional[List[_ORU_R01_PATIENT_OBSERVATION]] = Field(
        default=None,
        title="PATIENT_OBSERVATION",
        description="Optional, repeating",
    )

    VISIT: Optional[_ORU_R01_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
