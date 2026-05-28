"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ADT_A20
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.NPU import NPU
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EVN = EVN
_MSH = MSH
_NPU = NPU
_SFT = SFT
_UAC = UAC


class ADT_A20(BaseModel):
    """HL7 v2 ADT_A20 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        NPU (NPU): required
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

    EVN: _EVN = Field(
        default=...,
        title="EVN",
        description="Required",
    )

    NPU: _NPU = Field(
        default=...,
        title="NPU",
        description="Required",
    )

    model_config = {"populate_by_name": True}
