"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ESR_U02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EQU = EQU
_MSH = MSH
_SFT = SFT
_UAC = UAC


class ESR_U02(BaseModel):
    """HL7 v2 ESR_U02 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EQU (EQU): required
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

    EQU: _EQU = Field(
        default=...,
        title="EQU",
        description="Required",
    )

    model_config = {"populate_by_name": True}
