"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RRD_O14.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PID import PID

_NTE = NTE
_PID = PID


class RRD_O14_PATIENT(BaseModel):
    """HL7 v2 RRD_O14.PATIENT group.

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
