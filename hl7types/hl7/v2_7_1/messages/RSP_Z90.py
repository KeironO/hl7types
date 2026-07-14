"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RSP_Z90
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QPD import QPD
from ..segments.RCP import RCP
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.RSP_Z90_QUERY_RESPONSE import RSP_Z90_QUERY_RESPONSE

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RCP = RCP
_RSP_Z90_QUERY_RESPONSE = RSP_Z90_QUERY_RESPONSE
_SFT = SFT
_UAC = UAC


class RSP_Z90(HL7Model):
    """Lab Results History (Response) (S15.3.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
        QUERY_RESPONSE (List[RSP_Z90_QUERY_RESPONSE]): required
        DSC (DSC): Continuation Pointer, required
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

    RCP: _RCP = Field(
        title="RCP",
        description="Response Control Parameter",
    )

    QUERY_RESPONSE: List[_RSP_Z90_QUERY_RESPONSE] = Field(
        min_length=1,
        title="QUERY_RESPONSE",
    )

    DSC: _DSC = Field(
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = {"populate_by_name": True}
