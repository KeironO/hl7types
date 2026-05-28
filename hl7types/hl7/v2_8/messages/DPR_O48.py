"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DPR_O48
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.DPR_O48_DONATION import DPR_O48_DONATION
from ..groups.DPR_O48_DONATION_ORDER import DPR_O48_DONATION_ORDER
from ..groups.DPR_O48_DONOR import DPR_O48_DONOR
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DPR_O48_DONATION = DPR_O48_DONATION
_DPR_O48_DONATION_ORDER = DPR_O48_DONATION_ORDER
_DPR_O48_DONOR = DPR_O48_DONOR
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DPR_O48(BaseModel):
    """HL7 v2 DPR_O48 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        DONOR (Optional[DPR_O48_DONOR]): optional
        DONATION_ORDER (List[DPR_O48_DONATION_ORDER]): required
        DONATION (Optional[DPR_O48_DONATION]): optional
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

    DONOR: _DPR_O48_DONOR | None = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    DONATION_ORDER: list[_DPR_O48_DONATION_ORDER] = Field(
        default=...,
        title="DONATION_ORDER",
        description="Required, repeating",
    )

    DONATION: _DPR_O48_DONATION | None = Field(
        default=None,
        title="DONATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
