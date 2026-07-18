"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: QBP_Q13
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.RCP import RCP
from ..segments.RDF import RDF
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.QBP_Q13_QBP import QBP_Q13_QBP

_DSC = DSC
_MSH = MSH
_QBP_Q13_QBP = QBP_Q13_QBP
_QPD = QPD
_RCP = RCP
_RDF = RDF
_SFT = SFT
_UAC = UAC


class QBP_Q13(HL7Model):
    """QBP - Query by parameter requesting an  RTB - tabular response (S15.3.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
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

    model_config = ConfigDict(populate_by_name=True)
