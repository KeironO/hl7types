"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E01.PATIENT_INFO
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ACC import ACC
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from .EHC_E01_DIAGNOSIS import EHC_E01_DIAGNOSIS
from .EHC_E01_INSURANCE import EHC_E01_INSURANCE

_ACC = ACC
_EHC_E01_DIAGNOSIS = EHC_E01_DIAGNOSIS
_EHC_E01_INSURANCE = EHC_E01_INSURANCE
_OBX = OBX
_PID = PID
_PV1 = PV1
_PV2 = PV2


class EHC_E01_PATIENT_INFO(BaseModel):
    """HL7 v2 EHC_E01.PATIENT_INFO group.

    Attributes:
        PID (PID): required
        PV1 (Optional[PV1]): optional
        PV2 (Optional[PV2]): optional
        ACC (Optional[List[ACC]]): optional
        INSURANCE (List[EHC_E01_INSURANCE]): required
        DIAGNOSIS (Optional[List[EHC_E01_DIAGNOSIS]]): optional
        OBX (Optional[List[OBX]]): optional
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

    PV2: _PV2 | None = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    ACC: list[_ACC] | None = Field(
        default=None,
        title="ACC",
        description="Optional, repeating",
    )

    INSURANCE: list[_EHC_E01_INSURANCE] = Field(
        default=...,
        title="INSURANCE",
        description="Required, repeating",
    )

    DIAGNOSIS: list[_EHC_E01_DIAGNOSIS] | None = Field(
        default=None,
        title="DIAGNOSIS",
        description="Optional, repeating",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
