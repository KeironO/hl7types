"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OMD_O03.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from ..segments.GT1 import GT1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT
from .OMD_O03_INSURANCE import OMD_O03_INSURANCE
from .OMD_O03_PATIENT_VISIT import OMD_O03_PATIENT_VISIT

_AL1 = AL1
_GT1 = GT1
_NTE = NTE
_OMD_O03_INSURANCE = OMD_O03_INSURANCE
_OMD_O03_PATIENT_VISIT = OMD_O03_PATIENT_VISIT
_PD1 = PD1
_PID = PID
_PRT = PRT


class OMD_O03_PATIENT(BaseModel):
    """HL7 v2 OMD_O03.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT_VISIT (Optional[OMD_O03_PATIENT_VISIT]): optional
        INSURANCE (Optional[List[OMD_O03_INSURANCE]]): optional
        GT1 (Optional[GT1]): optional
        AL1 (Optional[List[AL1]]): optional
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

    PATIENT_VISIT: _OMD_O03_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    INSURANCE: list[_OMD_O03_INSURANCE] | None = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    GT1: _GT1 | None = Field(
        default=None,
        title="GT1",
        description="Optional",
    )

    AL1: list[_AL1] | None = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
