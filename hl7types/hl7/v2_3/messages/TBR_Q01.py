"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: TBR_Q01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.RDF import RDF
from ..segments.RDT import RDT

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_RDF = RDF
_RDT = RDT


class TBR_Q01(HL7Model):
    """QRY/DSR - Query sent for immediate response.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        ERR (Optional[ERR]): Error segment, optional
        QAK (QAK): Query Acknowledgement, required
        RDF (RDF): Table Row Definition, required
        RDT (List[RDT]): Table Row Data, required
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message acknowledgement segment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error segment",
    )

    QAK: _QAK = Field(
        title="QAK",
        description="Query Acknowledgement",
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
        description="Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
