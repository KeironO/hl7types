"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCR_I16.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PD1 import PD1
from ..segments.PID import PID

_PD1 = PD1
_PID = PID


class CCR_I16_PATIENT(BaseModel):
    """HL7 v2 CCR_I16.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
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

    model_config = {"populate_by_name": True}
