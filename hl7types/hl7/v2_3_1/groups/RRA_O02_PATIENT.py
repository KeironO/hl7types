"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRA_O02.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PID import PID

_NTE = NTE
_PID = PID


class RRA_O02_PATIENT(HL7Model):
    """HL7 v2 RRA_O02.PATIENT group.

    Attributes:
        PID (PID): PID - patient identification segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)
