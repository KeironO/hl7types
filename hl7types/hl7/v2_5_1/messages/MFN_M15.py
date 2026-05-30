"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFN_M15
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

from ..groups.MFN_M15_MF_INV_ITEM import MFN_M15_MF_INV_ITEM

_MFI = MFI
_MFN_M15_MF_INV_ITEM = MFN_M15_MF_INV_ITEM
_MSH = MSH
_SFT = SFT


class MFN_M15(HL7Model):
    """HL7 v2 MFN_M15 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MFI (MFI): required
        MF_INV_ITEM (List[MFN_M15_MF_INV_ITEM]): required
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

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF_INV_ITEM: List[_MFN_M15_MF_INV_ITEM] = Field(
        default=...,
        title="MF_INV_ITEM",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
