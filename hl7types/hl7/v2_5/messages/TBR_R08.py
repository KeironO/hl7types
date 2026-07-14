"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: TBR_R08
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
from ..segments.RDF import RDF
from ..segments.RDT import RDT
from ..segments.SFT import SFT

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_RDF = RDF
_RDT = RDT
_SFT = SFT


class TBR_R08(HL7Model):
    """HL7 v2 TBR_R08 message.

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        RDF (RDF): Table Row Definition, required
        RDT (List[RDT]): Table Row Data, required
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

    RDF: _RDF = Field(
        title="RDF",
        description="Table Row Definition",
    )

    RDT: List[_RDT] = Field(
        min_length=1,
        title="RDT",
        description="Table Row Data",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = {"populate_by_name": True}
