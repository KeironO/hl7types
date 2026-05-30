"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PMU_B08
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class PMU_B08(HL7Model):
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

    STF: _STF = Field(
        default=...,
        title="STF",
        description="Required",
    )

    PRA: Optional[_PRA] = Field(
        default=None,
        title="PRA",
        description="Optional",
    )

    CER: Optional[List[_CER]] = Field(
        default=None,
        title="CER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
