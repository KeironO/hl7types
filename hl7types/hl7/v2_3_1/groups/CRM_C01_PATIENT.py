"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
from ..segments.PV1 import PV1

_CSP = CSP
_CSR = CSR
_PID = PID
_PV1 = PV1


class CRM_C01_PATIENT(HL7Model):
    """HL7 v2 CRM_C01.PATIENT group.

    Attributes:
        PID (PID): PID - patient identification segment, required
        PV1 (Optional[PV1]): PV1 - patient visit segment-, optional
        CSR (CSR): CSR - clinical study registration segment, required
        CSP (Optional[List[CSP]]): CSP - clinical study phase segment, optional
    """

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="PV1 - patient visit segment-",
    )

    CSR: _CSR = Field(
        title="CSR",
        description="CSR - clinical study registration segment",
    )

    CSP: Optional[List[_CSP]] = Field(
        default=None,
        title="CSP",
        description="CSP - clinical study phase segment",
    )

    model_config = {"populate_by_name": True}
