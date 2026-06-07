"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DPR_O48
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.DPR_O48_DONATION import DPR_O48_DONATION
from ..groups.DPR_O48_DONATION_ORDER import DPR_O48_DONATION_ORDER
from ..groups.DPR_O48_DONOR import DPR_O48_DONOR

_DPR_O48_DONATION = DPR_O48_DONATION
_DPR_O48_DONATION_ORDER = DPR_O48_DONATION_ORDER
_DPR_O48_DONOR = DPR_O48_DONOR
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DPR_O48(HL7Model):
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

    DONOR: Optional[_DPR_O48_DONOR] = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    DONATION_ORDER: List[_DPR_O48_DONATION_ORDER] = Field(
        min_length=1,
        title="DONATION_ORDER",
        description="Required, repeating",
    )

    DONATION: Optional[_DPR_O48_DONATION] = Field(
        default=None,
        title="DONATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
