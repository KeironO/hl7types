"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PMU_B03
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.STF import STF

_EVN = EVN
_MSH = MSH
_SFT = SFT
_STF = STF


class PMU_B03(BaseModel):
    """HL7 v2 PMU_B03 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EVN (EVN): required
        STF (STF): required
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

    EVN: _EVN = Field(
        default=...,
        title="EVN",
        description="Required",
    )

    STF: _STF = Field(
        default=...,
        title="STF",
        description="Required",
    )

    model_config = {"populate_by_name": True}
