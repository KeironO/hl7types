"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E24
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.EHC_E24_AUTHORIZATION_RESPONSE_INFO import EHC_E24_AUTHORIZATION_RESPONSE_INFO
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EHC_E24_AUTHORIZATION_RESPONSE_INFO = EHC_E24_AUTHORIZATION_RESPONSE_INFO
_ERR = ERR
_MSA = MSA
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EHC_E24(BaseModel):
    """HL7 v2 EHC_E24 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        AUTHORIZATION_RESPONSE_INFO (EHC_E24_AUTHORIZATION_RESPONSE_INFO): required
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

    UAC: list[_UAC] | None = Field(
        default=None,
        title="UAC",
        description="Optional, repeating",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: list[_ERR] | None = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    AUTHORIZATION_RESPONSE_INFO: _EHC_E24_AUTHORIZATION_RESPONSE_INFO = Field(
        default=...,
        title="AUTHORIZATION_RESPONSE_INFO",
        description="Required",
    )

    model_config = {"populate_by_name": True}
