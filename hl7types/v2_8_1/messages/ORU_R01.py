"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORU_R01
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.ORU_R01_PATIENT_RESULT import ORU_R01_PATIENT_RESULT

_DSC = DSC
_MSH = MSH
_ORU_R01_PATIENT_RESULT = ORU_R01_PATIENT_RESULT
_SFT = SFT
_UAC = UAC


class ORU_R01(BaseModel):
    """HL7 v2 ORU_R01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        PATIENT_RESULT (List[ORU_R01_PATIENT_RESULT]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    PATIENT_RESULT: List[_ORU_R01_PATIENT_RESULT] = Field(
        default=...,
        title="PATIENT_RESULT",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
