"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DEO_O45
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.DEO_O45_DONOR import DEO_O45_DONOR
from ..groups.DEO_O45_DONOR_ORDER import DEO_O45_DONOR_ORDER
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DEO_O45_DONOR = DEO_O45_DONOR
_DEO_O45_DONOR_ORDER = DEO_O45_DONOR_ORDER
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DEO_O45(BaseModel):
    """HL7 v2 DEO_O45 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        DONOR (Optional[DEO_O45_DONOR]): optional
        DONOR_ORDER (List[DEO_O45_DONOR_ORDER]): required
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

    DONOR: _DEO_O45_DONOR | None = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    DONOR_ORDER: list[_DEO_O45_DONOR_ORDER] = Field(
        default=...,
        title="DONOR_ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
