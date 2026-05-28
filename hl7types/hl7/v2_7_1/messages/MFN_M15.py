"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: MFN_M15
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.MFN_M15_MF_INV_ITEM import MFN_M15_MF_INV_ITEM
from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MFI = MFI
_MFN_M15_MF_INV_ITEM = MFN_M15_MF_INV_ITEM
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M15(BaseModel):
    """HL7 v2 MFN_M15 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MFI (MFI): required
        MF_INV_ITEM (List[MFN_M15_MF_INV_ITEM]): required
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

    MF_INV_ITEM: list[_MFN_M15_MF_INV_ITEM] = Field(
        default=...,
        title="MF_INV_ITEM",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
