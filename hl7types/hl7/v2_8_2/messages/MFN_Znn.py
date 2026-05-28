"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_Znn
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.MFN_Znn_MF_SITE_DEFINED import MFN_Znn_MF_SITE_DEFINED

_MFI = MFI
_MFN_Znn_MF_SITE_DEFINED = MFN_Znn_MF_SITE_DEFINED
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_Znn(BaseModel):
    """HL7 v2 MFN_Znn message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MFI (MFI): required
        MF_SITE_DEFINED (List[MFN_Znn_MF_SITE_DEFINED]): required
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

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF_SITE_DEFINED: List[_MFN_Znn_MF_SITE_DEFINED] = Field(
        default=...,
        title="MF_SITE_DEFINED",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
