"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RAR_RAR.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PID import PID

_NTE = NTE
_PID = PID


class RAR_RAR_PATIENT(BaseModel):
    """HL7 v2 RAR_RAR.PATIENT group.

    Attributes:
        PID (PID): required
        NTE (Optional[List[NTE]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
