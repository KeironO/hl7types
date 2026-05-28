"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: BRT_O32
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.BRT_O32_RESPONSE import BRT_O32_RESPONSE
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

_BRT_O32_RESPONSE = BRT_O32_RESPONSE
_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_SFT = SFT


class BRT_O32(BaseModel):
    """HL7 v2 BRT_O32 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[List[NTE]]): optional
        RESPONSE (Optional[BRT_O32_RESPONSE]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
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

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RESPONSE: _BRT_O32_RESPONSE | None = Field(
        default=None,
        title="RESPONSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
