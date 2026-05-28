"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RSP_E03
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RSP_E03_QUERY_ACK import RSP_E03_QUERY_ACK
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_ERR = ERR
_MSA = MSA
_MSH = MSH
_RSP_E03_QUERY_ACK = RSP_E03_QUERY_ACK
_SFT = SFT
_UAC = UAC


class RSP_E03(BaseModel):
    """HL7 v2 RSP_E03 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        QUERY_ACK (RSP_E03_QUERY_ACK): required
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

    QUERY_ACK: _RSP_E03_QUERY_ACK = Field(
        default=...,
        title="QUERY_ACK",
        description="Required",
    )

    model_config = {"populate_by_name": True}
