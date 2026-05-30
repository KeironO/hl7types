"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: VXX_V02.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NK1 import NK1
from ..segments.PID import PID

_NK1 = NK1
_PID = PID


class VXX_V02_PATIENT(HL7Model):
    """HL7 v2 VXX_V02.PATIENT group.

    Attributes:
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
