"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORU_R03.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.PV1 import PV1

_NTE = NTE
_PID = PID
_PV1 = PV1


class ORU_R03_PATIENT(BaseModel):
    """HL7 v2 ORU_R03.PATIENT group.

    Attributes:
        PID (PID): required
        NTE (Optional[List[NTE]]): optional
        PV1 (Optional[PV1]): optional
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

    PV1: _PV1 | None = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
