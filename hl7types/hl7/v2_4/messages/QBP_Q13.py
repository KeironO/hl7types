"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Q13
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

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


class QBP_Q13(BaseModel):
    """HL7 v2 QBP_Q13 message.

    Attributes:
        MSH (MSH): required
        QPD (QPD): required
        QBP (Optional[QBP_Q13_QBP]): optional
        RDF (Optional[RDF]): optional
        RCP (RCP): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    QPD: _QPD = Field(
        default=...,
        title="QPD",
        description="Required",
    )

    QBP: Optional[_QBP_Q13_QBP] = Field(
        default=None,
        title="QBP",
        description="Optional",
    )

    RDF: Optional[_RDF] = Field(
        default=None,
        title="RDF",
        description="Optional",
    )

    RCP: _RCP = Field(
        default=...,
        title="RCP",
        description="Required",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
