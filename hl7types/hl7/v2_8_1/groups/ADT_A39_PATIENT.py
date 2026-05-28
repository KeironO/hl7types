"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ADT_A39.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.MRG import MRG
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1

_MRG = MRG
_PD1 = PD1
_PID = PID
_PV1 = PV1


class ADT_A39_PATIENT(BaseModel):
    """HL7 v2 ADT_A39.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        MRG (MRG): required
        PV1 (Optional[PV1]): optional
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

    MRG: _MRG = Field(
        default=...,
        title="MRG",
        description="Required",
    )

    PV1: _PV1 | None = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
