"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z88.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .RSP_Z88_ALLERGY import RSP_Z88_ALLERGY
from .RSP_Z88_COMMON_ORDER import RSP_Z88_COMMON_ORDER

_NTE = NTE
_PD1 = PD1
_PID = PID
_RSP_Z88_ALLERGY = RSP_Z88_ALLERGY
_RSP_Z88_COMMON_ORDER = RSP_Z88_COMMON_ORDER


class RSP_Z88_PATIENT(HL7Model):
    """HL7 v2 RSP_Z88.PATIENT group.

    Attributes:
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        ALLERGY (Optional[RSP_Z88_ALLERGY]): optional
        COMMON_ORDER (List[RSP_Z88_COMMON_ORDER]): required
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

    ALLERGY: Optional[_RSP_Z88_ALLERGY] = Field(
        default=None,
        title="ALLERGY",
    )

    COMMON_ORDER: List[_RSP_Z88_COMMON_ORDER] = Field(
        min_length=1,
        title="COMMON_ORDER",
    )

    model_config = {"populate_by_name": True}
