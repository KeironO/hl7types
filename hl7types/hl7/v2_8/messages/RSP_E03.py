"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_E03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class RSP_E03(HL7Model):
    """HealthCare Services Invoice Status (S15.3.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[List[UAC]]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        QUERY_ACK_IPR (RSP_E03_QUERY_ACK_IPR): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[List[_UAC]] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    QUERY_ACK_IPR: _RSP_E03_QUERY_ACK_IPR = Field(
        title="QUERY_ACK_IPR",
    )

    model_config = {"populate_by_name": True}
