"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RRA_O18
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RRA_O18_RESPONSE import RRA_O18_RESPONSE
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_RRA_O18_RESPONSE = RRA_O18_RESPONSE
_SFT = SFT
_UAC = UAC


class RRA_O18(BaseModel):
    """HL7 v2 RRA_O18 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        RESPONSE (Optional[RRA_O18_RESPONSE]): optional
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

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RESPONSE: _RRA_O18_RESPONSE | None = Field(
        default=None,
        title="RESPONSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
