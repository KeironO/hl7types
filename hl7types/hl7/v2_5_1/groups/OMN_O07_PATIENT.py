"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OMN_O07.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from ..segments.GT1 import GT1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from .OMN_O07_INSURANCE import OMN_O07_INSURANCE
from .OMN_O07_PATIENT_VISIT import OMN_O07_PATIENT_VISIT

_AL1 = AL1
_GT1 = GT1
_NTE = NTE
_OMN_O07_INSURANCE = OMN_O07_INSURANCE
_OMN_O07_PATIENT_VISIT = OMN_O07_PATIENT_VISIT
_PD1 = PD1
_PID = PID


class OMN_O07_PATIENT(BaseModel):
    """HL7 v2 OMN_O07.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT_VISIT (Optional[OMN_O07_PATIENT_VISIT]): optional
        INSURANCE (Optional[List[OMN_O07_INSURANCE]]): optional
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

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT_VISIT: _OMN_O07_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    INSURANCE: list[_OMN_O07_INSURANCE] | None = Field(
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
