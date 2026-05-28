"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DEL_O46
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DON import DON
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.DEL_O46_DONOR import DEL_O46_DONOR

_DEL_O46_DONOR = DEL_O46_DONOR
_DON = DON
_MSH = MSH
_NTE = NTE
_SFT = SFT
_UAC = UAC


class DEL_O46(BaseModel):
    """HL7 v2 DEL_O46 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        DONOR (Optional[DEL_O46_DONOR]): optional
        DON (DON): required
        NTE (Optional[List[NTE]]): optional
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

    DONOR: Optional[_DEL_O46_DONOR] = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    DON: _DON = Field(
        default=...,
        title="DON",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
