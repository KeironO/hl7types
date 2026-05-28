"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E20.PAT_INFO
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ACC import ACC
from ..segments.OBX import OBX
from ..segments.PID import PID
from .EHC_E20_DIAGNOSIS import EHC_E20_DIAGNOSIS
from .EHC_E20_INSURANCE import EHC_E20_INSURANCE

_ACC = ACC
_EHC_E20_DIAGNOSIS = EHC_E20_DIAGNOSIS
_EHC_E20_INSURANCE = EHC_E20_INSURANCE
_OBX = OBX
_PID = PID


class EHC_E20_PAT_INFO(BaseModel):
    """HL7 v2 EHC_E20.PAT_INFO group.

    Attributes:
        PID (PID): required
        ACC (Optional[List[ACC]]): optional
        INSURANCE (List[EHC_E20_INSURANCE]): required
        DIAGNOSIS (Optional[List[EHC_E20_DIAGNOSIS]]): optional
        OBX (Optional[List[OBX]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    ACC: list[_ACC] | None = Field(
        default=None,
        title="ACC",
        description="Optional, repeating",
    )

    INSURANCE: list[_EHC_E20_INSURANCE] = Field(
        default=...,
        title="INSURANCE",
        description="Required, repeating",
    )

    DIAGNOSIS: list[_EHC_E20_DIAGNOSIS] | None = Field(
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
