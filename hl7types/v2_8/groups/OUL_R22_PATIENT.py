"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OUL_R22.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

from .OUL_R22_PATIENT_OBSERVATION import OUL_R22_PATIENT_OBSERVATION
from .OUL_R22_VISIT import OUL_R22_VISIT

_ARV = ARV
_NTE = NTE
_OUL_R22_PATIENT_OBSERVATION = OUL_R22_PATIENT_OBSERVATION
_OUL_R22_VISIT = OUL_R22_VISIT
_PD1 = PD1
_PID = PID
_PRT = PRT


class OUL_R22_PATIENT(BaseModel):
    """HL7 v2 OUL_R22.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT_OBSERVATION (Optional[List[OUL_R22_PATIENT_OBSERVATION]]): optional
        VISIT (Optional[OUL_R22_VISIT]): optional
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

    PATIENT_OBSERVATION: Optional[List[_OUL_R22_PATIENT_OBSERVATION]] = Field(
        default=None,
        title="PATIENT_OBSERVATION",
        description="Optional, repeating",
    )

    VISIT: Optional[_OUL_R22_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
