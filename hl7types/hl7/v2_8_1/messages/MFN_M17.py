"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MFN_M17
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.MFN_M17_MF_DRG import MFN_M17_MF_DRG
from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MFI = MFI
_MFN_M17_MF_DRG = MFN_M17_MF_DRG
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M17(BaseModel):
    """HL7 v2 MFN_M17 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MFI (MFI): required
        MF_DRG (List[MFN_M17_MF_DRG]): required
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

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF_DRG: list[_MFN_M17_MF_DRG] = Field(
        default=...,
        title="MF_DRG",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
