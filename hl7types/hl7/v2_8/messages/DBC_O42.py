"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DBC_O42
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.DBC_O42_DONOR import DBC_O42_DONOR
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DBC_O42_DONOR = DBC_O42_DONOR
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DBC_O42(BaseModel):
    """HL7 v2 DBC_O42 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        DONOR (Optional[DBC_O42_DONOR]): optional
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

    DONOR: _DBC_O42_DONOR | None = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
