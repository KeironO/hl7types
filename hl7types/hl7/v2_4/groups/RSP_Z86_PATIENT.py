"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z86.PATIENT
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

from .RSP_Z86_COMMON_ORDER import RSP_Z86_COMMON_ORDER

_AL1 = AL1
_NTE = NTE
_PD1 = PD1
_PID = PID
_RSP_Z86_COMMON_ORDER = RSP_Z86_COMMON_ORDER


class RSP_Z86_PATIENT(HL7Model):
    """HL7 v2 RSP_Z86.PATIENT group.

    Attributes:
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        COMMON_ORDER (List[RSP_Z86_COMMON_ORDER]): required
    """

    PID: _PID = Field(
        title="PID",
        description="Patient identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="patient additional demographic",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient allergy information",
    )

    COMMON_ORDER: List[_RSP_Z86_COMMON_ORDER] = Field(
        min_length=1,
        title="COMMON_ORDER",
    )

    model_config = {"populate_by_name": True}
