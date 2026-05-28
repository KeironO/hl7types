"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DRG_O43
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.DRG_O43_DONOR import DRG_O43_DONOR
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

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

    DONOR: _DRG_O43_DONOR | None = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
