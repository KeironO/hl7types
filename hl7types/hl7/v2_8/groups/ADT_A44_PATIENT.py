"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ADT_A44.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.MRG import MRG
from ..segments.PD1 import PD1
from ..segments.PID import PID

_ARV = ARV
_MRG = MRG
_PD1 = PD1
_PID = PID


class ADT_A44_PATIENT(BaseModel):
    """HL7 v2 ADT_A44.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        ARV (Optional[List[ARV]]): optional
        MRG (MRG): required
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

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    MRG: _MRG = Field(
        default=...,
        title="MRG",
        description="Required",
    )

    model_config = {"populate_by_name": True}
