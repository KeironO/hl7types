"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DBC_O42
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.DBC_O42_DONOR import DBC_O42_DONOR

_DBC_O42_DONOR = DBC_O42_DONOR
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DBC_O42(HL7Model):
    """DBU - Update Donor Record Message (S4.16.4).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        DONOR (Optional[DBC_O42_DONOR]): optional
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

    DONOR: Optional[_DBC_O42_DONOR] = Field(
        default=None,
        title="DONOR",
    )

    model_config = ConfigDict(populate_by_name=True)
