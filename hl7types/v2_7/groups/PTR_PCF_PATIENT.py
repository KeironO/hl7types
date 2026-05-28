"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PTR_PCF.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PID import PID

from .PTR_PCF_PATHWAY import PTR_PCF_PATHWAY
from .PTR_PCF_PATIENT_VISIT import PTR_PCF_PATIENT_VISIT

_PID = PID
_PTR_PCF_PATHWAY = PTR_PCF_PATHWAY
_PTR_PCF_PATIENT_VISIT = PTR_PCF_PATIENT_VISIT


class PTR_PCF_PATIENT(BaseModel):
    """HL7 v2 PTR_PCF.PATIENT group.

    Attributes:
        PID (PID): required
        PATIENT_VISIT (Optional[PTR_PCF_PATIENT_VISIT]): optional
        PATHWAY (List[PTR_PCF_PATHWAY]): required
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: Optional[_PTR_PCF_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    PATHWAY: List[_PTR_PCF_PATHWAY] = Field(
        default=...,
        title="PATHWAY",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
