"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DRG_O43
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.DRG_O43_DONOR import DRG_O43_DONOR

_DRG_O43_DONOR = DRG_O43_DONOR
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DRG_O43(HL7Model):
    """General Order Message with Document Payload Acknowledgement Message (S4.16.10).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        DONOR (Optional[DRG_O43_DONOR]): optional
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

    DONOR: Optional[_DRG_O43_DONOR] = Field(
        default=None,
        title="DONOR",
    )

    model_config = {"populate_by_name": True}
