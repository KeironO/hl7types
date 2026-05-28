"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PMU_B01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

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


class PMU_B01(BaseModel):
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

    SFT: list[_SFT] | None = Field(
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

    PRA: list[_PRA] | None = Field(
        default=None,
        title="PRA",
        description="Optional, repeating",
    )

    ORG: list[_ORG] | None = Field(
        default=None,
        title="ORG",
        description="Optional, repeating",
    )

    AFF: list[_AFF] | None = Field(
        default=None,
        title="AFF",
        description="Optional, repeating",
    )

    LAN: list[_LAN] | None = Field(
        default=None,
        title="LAN",
        description="Optional, repeating",
    )

    EDU: list[_EDU] | None = Field(
        default=None,
        title="EDU",
        description="Optional, repeating",
    )

    CER: list[_CER] | None = Field(
        default=None,
        title="CER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
