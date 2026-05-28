"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DBC_O41.DONOR
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID

_AL1 = AL1
_ARV = ARV
_NTE = NTE
_OBX = OBX
_PD1 = PD1
_PID = PID


class DBC_O41_DONOR(BaseModel):
    """HL7 v2 DBC_O41.DONOR group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        OBX (Optional[List[OBX]]): optional
        NTE (Optional[List[NTE]]): optional
        ARV (Optional[List[ARV]]): optional
        AL1 (Optional[List[AL1]]): optional
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

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    AL1: list[_AL1] | None = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
