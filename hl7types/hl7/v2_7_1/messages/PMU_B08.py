"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PMU_B08
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CER import CER
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PRA import PRA
from ..segments.SFT import SFT
from ..segments.STF import STF
from ..segments.UAC import UAC

_CER = CER
_EVN = EVN
_MSH = MSH
_PRA = PRA
_SFT = SFT
_STF = STF
_UAC = UAC


class PMU_B08(BaseModel):
    """HL7 v2 PMU_B08 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        STF (STF): required
        PRA (Optional[PRA]): optional
        CER (Optional[List[CER]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
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

    PRA: _PRA | None = Field(
        default=None,
        title="PRA",
        description="Optional",
    )

    CER: list[_CER] | None = Field(
        default=None,
        title="CER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
