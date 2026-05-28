"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: UDM_Q05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.DSP import DSP
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.URD import URD
from ..segments.URS import URS

_DSC = DSC
_DSP = DSP
_MSH = MSH
_SFT = SFT
_URD = URD
_URS = URS


class UDM_Q05(BaseModel):
    """HL7 v2 UDM_Q05 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        URD (URD): required
        URS (Optional[URS]): optional
        DSP (List[DSP]): required
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

    URD: _URD = Field(
        default=...,
        title="URD",
        description="Required",
    )

    URS: Optional[_URS] = Field(
        default=None,
        title="URS",
        description="Optional",
    )

    DSP: List[_DSP] = Field(
        default=...,
        title="DSP",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
