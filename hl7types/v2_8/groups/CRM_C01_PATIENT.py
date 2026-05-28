"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CRM_C01.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.CSP import CSP
from ..segments.CSR import CSR
from ..segments.PID import PID
from ..segments.PRT import PRT

from .CRM_C01_PATIENT_VISIT import CRM_C01_PATIENT_VISIT

_ARV = ARV
_CRM_C01_PATIENT_VISIT = CRM_C01_PATIENT_VISIT
_CSP = CSP
_CSR = CSR
_PID = PID
_PRT = PRT


class CRM_C01_PATIENT(BaseModel):
    """HL7 v2 CRM_C01.PATIENT group.

    Attributes:
        PID (PID): required
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        PATIENT_VISIT (Optional[CRM_C01_PATIENT_VISIT]): optional
        CSR (CSR): required
        CSP (Optional[List[CSP]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
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

    PATIENT_VISIT: Optional[_CRM_C01_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    CSR: _CSR = Field(
        default=...,
        title="CSR",
        description="Required",
    )

    CSP: Optional[List[_CSP]] = Field(
        default=None,
        title="CSP",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
