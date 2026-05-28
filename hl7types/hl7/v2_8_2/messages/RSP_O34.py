"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RSP_O34
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

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


class RSP_O34(BaseModel):
    """HL7 v2 RSP_O34 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (QAK): required
        QPD (QPD): required
        DONOR (Optional[RSP_O34_DONOR]): optional
        DONATION (Optional[RSP_O34_DONATION]): optional
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    QAK: _QAK = Field(
        default=...,
        title="QAK",
        description="Required",
    )

    QPD: _QPD = Field(
        default=...,
        title="QPD",
        description="Required",
    )

    DONOR: Optional[_RSP_O34_DONOR] = Field(
        default=None,
        title="DONOR",
        description="Optional",
    )

    DONATION: Optional[_RSP_O34_DONATION] = Field(
        default=None,
        title="DONATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
