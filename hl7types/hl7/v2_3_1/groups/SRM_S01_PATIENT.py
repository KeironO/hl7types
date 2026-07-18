"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SRM_S01.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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


class SRM_S01_PATIENT(HL7Model):
    """HL7 v2 SRM_S01.PATIENT group.

    Attributes:
        PID (PID): PID - patient identification segment, required
        PV1 (Optional[PV1]): PV1 - patient visit segment-, optional
        PV2 (Optional[PV2]): PV2 - patient visit - additional information segment, optional
        OBX (Optional[List[OBX]]): OBX - observation/result segment, optional
        DG1 (Optional[List[DG1]]): DG1 - diagnosis segment, optional
    """

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="PV1 - patient visit segment-",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="PV2 - patient visit - additional information segment",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="OBX - observation/result segment",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="DG1 - diagnosis segment",
    )

    model_config = ConfigDict(populate_by_name=True)
