"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RSP_K11
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
from ..segments.SFT import SFT

from ..groups.RSP_K11_ROW_DEFINITION import RSP_K11_ROW_DEFINITION

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RSP_K11_ROW_DEFINITION = RSP_K11_ROW_DEFINITION
_SFT = SFT


class RSP_K11(HL7Model):
    """RSP - Segment pattern response in response to QBP^Q11 (S15.3.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        ROW_DEFINITION (Optional[RSP_K11_ROW_DEFINITION]): optional
        DSC (Optional[DSC]): Continuation Pointer, optional
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

    ROW_DEFINITION: Optional[_RSP_K11_ROW_DEFINITION] = Field(
        default=None,
        title="ROW_DEFINITION",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = {"populate_by_name": True}
