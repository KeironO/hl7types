"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OPU_R25.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT
from .OPU_R25_PATIENT_OBSERVATION import OPU_R25_PATIENT_OBSERVATION

_ARV = ARV
_OPU_R25_PATIENT_OBSERVATION = OPU_R25_PATIENT_OBSERVATION
_PD1 = PD1
_PID = PID
_PRT = PRT


class OPU_R25_PATIENT(BaseModel):
    """HL7 v2 OPU_R25.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        PATIENT_OBSERVATION (Optional[List[OPU_R25_PATIENT_OBSERVATION]]): optional
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

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    PATIENT_OBSERVATION: list[_OPU_R25_PATIENT_OBSERVATION] | None = Field(
        default=None,
        title="PATIENT_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
