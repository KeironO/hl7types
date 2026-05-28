"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OUL_R21.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

_NTE = NTE
_PD1 = PD1
_PID = PID


class OUL_R21_PATIENT(BaseModel):
    """HL7 v2 OUL_R21.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: _PD1 | None = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
