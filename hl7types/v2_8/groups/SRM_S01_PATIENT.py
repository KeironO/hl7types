"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: SRM_S01.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DG1 import DG1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

from .SRM_S01_OBSERVATION import SRM_S01_OBSERVATION

_DG1 = DG1
_PID = PID
_PV1 = PV1
_PV2 = PV2
_SRM_S01_OBSERVATION = SRM_S01_OBSERVATION


class SRM_S01_PATIENT(BaseModel):
    """HL7 v2 SRM_S01.PATIENT group.

    Attributes:
        PID (PID): required
        PV1 (Optional[PV1]): optional
        PV2 (Optional[PV2]): optional
        OBSERVATION (Optional[List[SRM_S01_OBSERVATION]]): optional
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

    OBSERVATION: Optional[List[_SRM_S01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
