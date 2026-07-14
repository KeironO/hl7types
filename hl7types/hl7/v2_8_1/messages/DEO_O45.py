"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DEO_O45
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.DEO_O45_DONATION_ORDER import DEO_O45_DONATION_ORDER
from ..groups.DEO_O45_DONOR import DEO_O45_DONOR

_DEO_O45_DONATION_ORDER = DEO_O45_DONATION_ORDER
_DEO_O45_DONOR = DEO_O45_DONOR
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DEO_O45(HL7Model):
    """Donor Eligibility Observations Message (S4.16.12).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        DONOR (Optional[DEO_O45_DONOR]): optional
        DONATION_ORDER (List[DEO_O45_DONATION_ORDER]): required
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

    DONOR: Optional[_DEO_O45_DONOR] = Field(
        default=None,
        title="DONOR",
    )

    DONATION_ORDER: List[_DEO_O45_DONATION_ORDER] = Field(
        min_length=1,
        title="DONATION_ORDER",
    )

    model_config = {"populate_by_name": True}
