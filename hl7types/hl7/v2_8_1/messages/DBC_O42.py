"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DBC_O42
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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

    DONOR: Optional[_DBC_O42_DONOR] = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
