"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SIU_S12.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DG1 import DG1
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_DG1 = DG1
_OBX = OBX
_PID = PID
_PV1 = PV1
_PV2 = PV2


class SIU_S12_PATIENT(HL7Model):
    """HL7 v2 SIU_S12.PATIENT group.

    Attributes:
        PID (PID): required
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

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
