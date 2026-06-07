"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: QBP_Q13
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
    """HL7 v2 QBP_Q13 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        QPD (QPD): required
        QBP (Optional[QBP_Q13_QBP]): optional
        RDF (Optional[RDF]): optional
        RCP (RCP): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    QPD: _QPD = Field(
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
        title="RCP",
        description="Required",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
