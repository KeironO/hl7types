"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_O34
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

from ..groups.RSP_O34_DONATION import RSP_O34_DONATION
from ..groups.RSP_O34_DONOR import RSP_O34_DONOR

_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RSP_O34_DONATION = RSP_O34_DONATION
_RSP_O34_DONOR = RSP_O34_DONOR
_SFT = SFT
_UAC = UAC


class RSP_O34(HL7Model):
    """ORL - Laboratory order response message to a multiple order related to single sp (S15.3.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        DONOR (Optional[RSP_O34_DONOR]): optional
        DONATION (Optional[RSP_O34_DONATION]): optional
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

    DONOR: Optional[_RSP_O34_DONOR] = Field(
        default=None,
        title="DONOR",
    )

    DONATION: Optional[_RSP_O34_DONATION] = Field(
        default=None,
        title="DONATION",
    )

    model_config = {"populate_by_name": True}
