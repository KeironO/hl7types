"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RAS_O17.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .RAS_O17_PATIENT_VISIT import RAS_O17_PATIENT_VISIT

_AL1 = AL1
_NTE = NTE
_PD1 = PD1
_PID = PID
_RAS_O17_PATIENT_VISIT = RAS_O17_PATIENT_VISIT


class RAS_O17_PATIENT(HL7Model):
    """HL7 v2 RAS_O17.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        AL1 (Optional[List[AL1]]): optional
        PATIENT_VISIT (Optional[RAS_O17_PATIENT_VISIT]): optional
    """

    PID: _PID = Field(
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

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    PATIENT_VISIT: Optional[_RAS_O17_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
