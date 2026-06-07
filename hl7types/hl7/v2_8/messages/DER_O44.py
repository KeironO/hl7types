"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DER_O44
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.DER_O44_DONOR import DER_O44_DONOR
from ..groups.DER_O44_DONOR_ORDER import DER_O44_DONOR_ORDER

_DER_O44_DONOR = DER_O44_DONOR
_DER_O44_DONOR_ORDER = DER_O44_DONOR_ORDER
_MSH = MSH
_SFT = SFT
_UAC = UAC


class DER_O44(HL7Model):
    """HL7 v2 DER_O44 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        DONOR (Optional[DER_O44_DONOR]): optional
        DONOR_ORDER (List[DER_O44_DONOR_ORDER]): required
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

    DONOR: Optional[_DER_O44_DONOR] = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    DONOR_ORDER: List[_DER_O44_DONOR_ORDER] = Field(
        min_length=1,
        title="DONOR_ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
