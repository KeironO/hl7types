"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: BAR_P06.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PID import PID
from ..segments.PV1 import PV1

_PID = PID
_PV1 = PV1


class BAR_P06_PATIENT(BaseModel):
    """HL7 v2 BAR_P06.PATIENT group.

    Attributes:
        PID (PID): required
        PV1 (Optional[PV1]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PV1: _PV1 | None = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
