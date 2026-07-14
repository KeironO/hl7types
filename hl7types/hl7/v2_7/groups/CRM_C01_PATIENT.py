"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CRM_C01.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CSP import CSP
from ..segments.CSR import CSR
from ..segments.PID import PID
from ..segments.PRT import PRT

from .CRM_C01_PATIENT_VISIT import CRM_C01_PATIENT_VISIT

_CRM_C01_PATIENT_VISIT = CRM_C01_PATIENT_VISIT
_CSP = CSP
_CSR = CSR
_PID = PID
_PRT = PRT


class CRM_C01_PATIENT(HL7Model):
    """HL7 v2 CRM_C01.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        PATIENT_VISIT (Optional[CRM_C01_PATIENT_VISIT]): optional
        CSR (CSR): Clinical Study Registration, required
        CSP (Optional[List[CSP]]): Clinical Study Phase, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    PATIENT_VISIT: Optional[_CRM_C01_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    CSR: _CSR = Field(
        title="CSR",
        description="Clinical Study Registration",
    )

    CSP: Optional[List[_CSP]] = Field(
        default=None,
        title="CSP",
        description="Clinical Study Phase",
    )

    model_config = {"populate_by_name": True}
