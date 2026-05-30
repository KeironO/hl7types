"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PMU_B01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AFF import AFF
from ..segments.CER import CER
from ..segments.EDU import EDU
from ..segments.EVN import EVN
from ..segments.LAN import LAN
from ..segments.MSH import MSH
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.SFT import SFT
from ..segments.STF import STF

_AFF = AFF
_CER = CER
_EDU = EDU
_EVN = EVN
_LAN = LAN
_MSH = MSH
_ORG = ORG
_PRA = PRA
_SFT = SFT
_STF = STF


class PMU_B01(HL7Model):
    """HL7 v2 PMU_B01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EVN (EVN): required
        STF (STF): required
        PRA (Optional[List[PRA]]): optional
        ORG (Optional[List[ORG]]): optional
        AFF (Optional[List[AFF]]): optional
        LAN (Optional[List[LAN]]): optional
        EDU (Optional[List[EDU]]): optional
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

    PRA: Optional[List[_PRA]] = Field(
        default=None,
        title="PRA",
        description="Optional, repeating",
    )

    ORG: Optional[List[_ORG]] = Field(
        default=None,
        title="ORG",
        description="Optional, repeating",
    )

    AFF: Optional[List[_AFF]] = Field(
        default=None,
        title="AFF",
        description="Optional, repeating",
    )

    LAN: Optional[List[_LAN]] = Field(
        default=None,
        title="LAN",
        description="Optional, repeating",
    )

    EDU: Optional[List[_EDU]] = Field(
        default=None,
        title="EDU",
        description="Optional, repeating",
    )

    CER: Optional[List[_CER]] = Field(
        default=None,
        title="CER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
