"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DEL_O46
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.DEL_O46_DONOR import DEL_O46_DONOR
from ..segments.DON import DON
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

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

    DONOR: _DEL_O46_DONOR | None = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    DON: _DON = Field(
        default=...,
        title="DON",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
