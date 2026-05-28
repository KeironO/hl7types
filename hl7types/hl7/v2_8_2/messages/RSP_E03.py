"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RSP_E03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.RSP_E03_QUERY_ACK_IPR import RSP_E03_QUERY_ACK_IPR

_ERR = ERR
_MSA = MSA
_MSH = MSH
_RSP_E03_QUERY_ACK_IPR = RSP_E03_QUERY_ACK_IPR
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
        QUERY_ACK_IPR (RSP_E03_QUERY_ACK_IPR): required
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

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    QUERY_ACK_IPR: _RSP_E03_QUERY_ACK_IPR = Field(
        default=...,
        title="QUERY_ACK_IPR",
        description="Required",
    )

    model_config = {"populate_by_name": True}
