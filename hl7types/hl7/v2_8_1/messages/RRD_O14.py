"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RRD_O14
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RRD_O14_RESPONSE import RRD_O14_RESPONSE
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
_RRD_O14_RESPONSE = RRD_O14_RESPONSE
_SFT = SFT
_UAC = UAC


class RRD_O14(BaseModel):
    """HL7 v2 RRD_O14 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        RESPONSE (Optional[RRD_O14_RESPONSE]): optional
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

    RESPONSE: _RRD_O14_RESPONSE | None = Field(
        default=None,
        title="RESPONSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
