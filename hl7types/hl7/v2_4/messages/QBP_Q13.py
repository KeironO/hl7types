"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Q13
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.RCP import RCP
from ..segments.RDF import RDF

from ..groups.QBP_Q13_QBP import QBP_Q13_QBP

_DSC = DSC
_MSH = MSH
_QBP_Q13_QBP = QBP_Q13_QBP
_QPD = QPD
_RCP = RCP
_RDF = RDF


class QBP_Q13(HL7Model):
    """quey by parameter/tabluar response (S15).

    Attributes:
        MSH (MSH): Message Header, required
        QPD (QPD): Query Parameter Definition, required
        QBP (Optional[QBP_Q13_QBP]): optional
        RDF (Optional[RDF]): Table Row Definition, optional
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    QPD: _QPD = Field(
        title="QPD",
        description="Query Parameter Definition",
    )

    QBP: Optional[_QBP_Q13_QBP] = Field(
        default=None,
        title="QBP",
    )

    RDF: Optional[_RDF] = Field(
        default=None,
        title="RDF",
        description="Table Row Definition",
    )

    RCP: _RCP = Field(
        title="RCP",
        description="Response Control Parameter",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = {"populate_by_name": True}
