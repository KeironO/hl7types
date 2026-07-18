"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MFN_M16
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class MFN_M16(HL7Model):
    """MFN/MFK - Master File Notification Inventory Item Enhanced (S8.10.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MFI (MFI): Master File Identification, required
        MATERIAL_ITEM_RECORD (List[MFN_M16_MATERIAL_ITEM_RECORD]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master File Identification",
    )

    MATERIAL_ITEM_RECORD: List[_MFN_M16_MATERIAL_ITEM_RECORD] = Field(
        min_length=1,
        title="MATERIAL_ITEM_RECORD",
    )

    model_config = ConfigDict(populate_by_name=True)
