"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DRG_O43
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.DRG_O43_DONOR import DRG_O43_DONOR

_DRG_O43_DONOR = DRG_O43_DONOR
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DRG_O43(BaseModel):
    """HL7 v2 DRG_O43 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        DONOR (Optional[DRG_O43_DONOR]): optional
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

    DONOR: Optional[_DRG_O43_DONOR] = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
