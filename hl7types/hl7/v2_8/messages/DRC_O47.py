"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DRC_O47
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.DRC_O47_DONATION_ORDER import DRC_O47_DONATION_ORDER
from ..groups.DRC_O47_DONOR import DRC_O47_DONOR
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DRC_O47_DONATION_ORDER = DRC_O47_DONATION_ORDER
_DRC_O47_DONOR = DRC_O47_DONOR
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DRC_O47(BaseModel):
    """HL7 v2 DRC_O47 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        DONOR (Optional[DRC_O47_DONOR]): optional
        DONATION_ORDER (List[DRC_O47_DONATION_ORDER]): required
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

    DONOR: _DRC_O47_DONOR | None = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    DONATION_ORDER: list[_DRC_O47_DONATION_ORDER] = Field(
        default=...,
        title="DONATION_ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
