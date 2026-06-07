"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OSR_Q06.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PID import PID

_NTE = NTE
_PID = PID


class OSR_Q06_PATIENT(HL7Model):
    """HL7 v2 OSR_Q06.PATIENT group.

    Attributes:
        PID (PID): required
        NTE (Optional[List[NTE]]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
