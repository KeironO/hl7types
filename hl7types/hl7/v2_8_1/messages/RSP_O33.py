"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_O33
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QPD import QPD
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.RSP_O33_DONOR import RSP_O33_DONOR

_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RSP_O33_DONOR = RSP_O33_DONOR
_SFT = SFT
_UAC = UAC


class RSP_O33(HL7Model):
    """OML - Laboratory order for multiple orders related to a single specimen (S15.3.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        DONOR (Optional[RSP_O33_DONOR]): optional
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    QAK: _QAK = Field(
        title="QAK",
        description="Query Acknowledgment",
    )

    QPD: _QPD = Field(
        title="QPD",
        description="Query Parameter Definition",
    )

    DONOR: Optional[_RSP_O33_DONOR] = Field(
        default=None,
        title="DONOR",
    )

    model_config = {"populate_by_name": True}
