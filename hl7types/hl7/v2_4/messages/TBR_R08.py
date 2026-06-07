"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_RDF = RDF
_RDT = RDT


class TBR_R08(HL7Model):
    """HL7 v2 TBR_R08 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (QAK): required
        RDF (RDF): required
        RDT (List[RDT]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Required",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    QAK: _QAK = Field(
        title="QAK",
        description="Required",
    )

    RDF: _RDF = Field(
        title="RDF",
        description="Required",
    )

    RDT: List[_RDT] = Field(
        min_length=1,
        title="RDT",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
