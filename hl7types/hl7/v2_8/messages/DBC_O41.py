"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DBC_O41
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.DBC_O41_DONOR import DBC_O41_DONOR

_DBC_O41_DONOR = DBC_O41_DONOR
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DBC_O41(BaseModel):
    """HL7 v2 DBC_O41 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        DONOR (Optional[DBC_O41_DONOR]): optional
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

    DONOR: Optional[_DBC_O41_DONOR] = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
