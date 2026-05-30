"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORU_R01.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .ORU_R01_VISIT import ORU_R01_VISIT

_NTE = NTE
_ORU_R01_VISIT = ORU_R01_VISIT
_PD1 = PD1
_PID = PID


class ORU_R01_PATIENT(HL7Model):
    """HL7 v2 ORU_R01.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        VISIT (Optional[ORU_R01_VISIT]): optional
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

    VISIT: Optional[_ORU_R01_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
