"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
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
from ..segments.UAC import UAC

from ..groups.MFN_M15_MF_INV_ITEM import MFN_M15_MF_INV_ITEM

_MFI = MFI
_MFN_M15_MF_INV_ITEM = MFN_M15_MF_INV_ITEM
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M15(HL7Model):
    """MFN/MFK - Inventory item master file notification (S8.10.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MFI (MFI): Master File Identification, required
        MF_INV_ITEM (List[MFN_M15_MF_INV_ITEM]): required
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

    MF_INV_ITEM: List[_MFN_M15_MF_INV_ITEM] = Field(
        min_length=1,
        title="MF_INV_ITEM",
    )

    model_config = {"populate_by_name": True}
