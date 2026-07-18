"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DRC_O47
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.DRC_O47_DONATION_ORDER import DRC_O47_DONATION_ORDER
from ..groups.DRC_O47_DONOR import DRC_O47_DONOR

_DRC_O47_DONATION_ORDER = DRC_O47_DONATION_ORDER
_DRC_O47_DONOR = DRC_O47_DONOR
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DRC_O47(HL7Model):
    """Donor Request to Collect Message (S4.16.14).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        DONOR (Optional[DRC_O47_DONOR]): optional
        DONATION_ORDER (List[DRC_O47_DONATION_ORDER]): required
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

    DONOR: Optional[_DRC_O47_DONOR] = Field(
        default=None,
        title="DONOR",
    )

    DONATION_ORDER: List[_DRC_O47_DONATION_ORDER] = Field(
        min_length=1,
        title="DONATION_ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
