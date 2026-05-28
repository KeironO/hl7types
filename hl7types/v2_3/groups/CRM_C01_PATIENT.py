"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CRM_C01.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CSP import CSP
from ..segments.CSR import CSR
from ..segments.PID import PID
from ..segments.PV1 import PV1

_CSP = CSP
_CSR = CSR
_PID = PID
_PV1 = PV1


class CRM_C01_PATIENT(BaseModel):
    """HL7 v2 CRM_C01.PATIENT group.

    Attributes:
        PID (PID): required
        PV1 (Optional[PV1]): optional
        CSR (CSR): required
        CSP (Optional[List[CSP]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
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
