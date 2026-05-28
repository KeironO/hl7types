"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORG_O20.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.PRT import PRT

_NTE = NTE
_PID = PID
_PRT = PRT


class ORG_O20_PATIENT(BaseModel):
    """HL7 v2 ORG_O20.PATIENT group.

    Attributes:
        PID (PID): required
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
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

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
