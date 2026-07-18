"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Qnn
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class QBP_Qnn(HL7Model):
    """HL7 v2 QBP_Qnn message.

    Attributes:
        MSH (MSH): Message Header, required
        QPD (QPD): Query Parameter Definition, required
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

    model_config = ConfigDict(populate_by_name=True)
