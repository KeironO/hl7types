"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SIU_S12.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DG1 import DG1
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_DG1 = DG1
_OBX = OBX
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2


class SIU_S12_PATIENT(BaseModel):
    """HL7 v2 SIU_S12.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PV1 (Optional[PV1]): optional
        PV2 (Optional[PV2]): optional
        OBX (Optional[List[OBX]]): optional
        DG1 (Optional[List[DG1]]): optional
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

    PV1: _PV1 | None = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    PV2: _PV2 | None = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    DG1: list[_DG1] | None = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
