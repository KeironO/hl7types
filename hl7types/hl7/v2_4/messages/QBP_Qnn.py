"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Qnn
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.RCP import RCP
from ..segments.RDF import RDF

_DSC = DSC
_MSH = MSH
_QPD = QPD
_RCP = RCP
_RDF = RDF


class QBP_Qnn(BaseModel):
    """HL7 v2 QBP_Qnn message.

    Attributes:
        MSH (MSH): required
        QPD (QPD): required
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

    RDF: _RDF | None = Field(
        default=None,
        title="RDF",
        description="Optional",
    )

    RCP: _RCP = Field(
        default=...,
        title="RCP",
        description="Required",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
