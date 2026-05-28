"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: MFN_M16
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.MFN_M16_MATERIAL_ITEM_RECORD import MFN_M16_MATERIAL_ITEM_RECORD

_MFI = MFI
_MFN_M16_MATERIAL_ITEM_RECORD = MFN_M16_MATERIAL_ITEM_RECORD
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M16(BaseModel):
    """HL7 v2 MFN_M16 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MFI (MFI): required
        MATERIAL_ITEM_RECORD (List[MFN_M16_MATERIAL_ITEM_RECORD]): required
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

    MATERIAL_ITEM_RECORD: List[_MFN_M16_MATERIAL_ITEM_RECORD] = Field(
        default=...,
        title="MATERIAL_ITEM_RECORD",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
