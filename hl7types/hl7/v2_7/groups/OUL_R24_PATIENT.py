"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OUL_R24.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT
from .OUL_R24_PATIENT_OBSERVATION import OUL_R24_PATIENT_OBSERVATION
from .OUL_R24_VISIT import OUL_R24_VISIT

_NTE = NTE
_OUL_R24_PATIENT_OBSERVATION = OUL_R24_PATIENT_OBSERVATION
_OUL_R24_VISIT = OUL_R24_VISIT
_PD1 = PD1
_PID = PID
_PRT = PRT


class OUL_R24_PATIENT(BaseModel):
    """HL7 v2 OUL_R24.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT_OBSERVATION (Optional[List[OUL_R24_PATIENT_OBSERVATION]]): optional
        VISIT (Optional[OUL_R24_VISIT]): optional
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

    PATIENT_OBSERVATION: list[_OUL_R24_PATIENT_OBSERVATION] | None = Field(
        default=None,
        title="PATIENT_OBSERVATION",
        description="Optional, repeating",
    )

    VISIT: _OUL_R24_VISIT | None = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
