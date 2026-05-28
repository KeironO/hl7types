"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E20
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.EHC_E20_AUTHORIZATION_REQUEST import EHC_E20_AUTHORIZATION_REQUEST

_EHC_E20_AUTHORIZATION_REQUEST = EHC_E20_AUTHORIZATION_REQUEST
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EHC_E20(BaseModel):
    """HL7 v2 EHC_E20 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        AUTHORIZATION_REQUEST (EHC_E20_AUTHORIZATION_REQUEST): required
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

    UAC: Optional[List[_UAC]] = Field(
        default=None,
        title="UAC",
        description="Optional, repeating",
    )

    AUTHORIZATION_REQUEST: _EHC_E20_AUTHORIZATION_REQUEST = Field(
        default=...,
        title="AUTHORIZATION_REQUEST",
        description="Required",
    )

    model_config = {"populate_by_name": True}
