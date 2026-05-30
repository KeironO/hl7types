"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OMI_O23.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.GT1 import GT1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .OMI_O23_INSURANCE import OMI_O23_INSURANCE
from .OMI_O23_PATIENT_VISIT import OMI_O23_PATIENT_VISIT

_AL1 = AL1
_GT1 = GT1
_NTE = NTE
_OMI_O23_INSURANCE = OMI_O23_INSURANCE
_OMI_O23_PATIENT_VISIT = OMI_O23_PATIENT_VISIT
_PD1 = PD1
_PID = PID


class OMI_O23_PATIENT(HL7Model):
    """HL7 v2 OMI_O23.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT_VISIT (Optional[OMI_O23_PATIENT_VISIT]): optional
        INSURANCE (Optional[List[OMI_O23_INSURANCE]]): optional
        GT1 (Optional[GT1]): optional
        AL1 (Optional[List[AL1]]): optional
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT_VISIT: Optional[_OMI_O23_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    INSURANCE: Optional[List[_OMI_O23_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    GT1: Optional[_GT1] = Field(
        default=None,
        title="GT1",
        description="Optional",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
