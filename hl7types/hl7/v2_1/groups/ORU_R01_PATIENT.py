"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORU_R01.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.PV1 import PV1

_NTE = NTE
_PID = PID
_PV1 = PV1


class ORU_R01_PATIENT(HL7Model):
    """HL7 v2 ORU_R01.PATIENT group.

    Attributes:
        PID (PID): PATIENT IDENTIFICATION, required
        NTE (Optional[List[NTE]]): NOTES AND COMMENTS, optional
        PV1 (Optional[PV1]): PATIENT VISIT, optional
    """

    PID: _PID = Field(
        title="PID",
        description="PATIENT IDENTIFICATION",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NOTES AND COMMENTS",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="PATIENT VISIT",
    )

    model_config = {"populate_by_name": True}
