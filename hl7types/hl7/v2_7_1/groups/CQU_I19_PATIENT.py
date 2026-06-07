"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CQU_I19.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PD1 import PD1
from ..segments.PID import PID

_PD1 = PD1
_PID = PID


class CQU_I19_PATIENT(HL7Model):
    """HL7 v2 CQU_I19.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
