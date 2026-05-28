"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R22.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID
from .OUL_R22_VISIT import OUL_R22_VISIT

_NTE = NTE
_OBX = OBX
_OUL_R22_VISIT = OUL_R22_VISIT
_PD1 = PD1
_PID = PID


class OUL_R22_PATIENT(BaseModel):
    """HL7 v2 OUL_R22.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        OBX (Optional[List[OBX]]): optional
        VISIT (Optional[OUL_R22_VISIT]): optional
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

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    VISIT: _OUL_R22_VISIT | None = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
