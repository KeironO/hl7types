"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CSU_C09
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.CSU_C09_PATIENT import CSU_C09_PATIENT

_CSU_C09_PATIENT = CSU_C09_PATIENT
_MSH = MSH
_SFT = SFT
_UAC = UAC


class CSU_C09(BaseModel):
    """HL7 v2 CSU_C09 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        PATIENT (List[CSU_C09_PATIENT]): required
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

    PATIENT: List[_CSU_C09_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
