"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: QBP_Q13
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.QPD import QPD
from ..segments.RCP import RCP
from ..segments.RDF import RDF
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DSC = DSC
_MSH = MSH
_PID = PID
_QPD = QPD
_RCP = RCP
_RDF = RDF
_SFT = SFT
_UAC = UAC


class QBP_Q13(BaseModel):
    """HL7 v2 QBP_Q13 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        QPD (QPD): required
        PID (Optional[PID]): optional
        RDF (Optional[RDF]): optional
        RCP (RCP): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    QPD: _QPD = Field(
        default=...,
        title="QPD",
        description="Required",
    )

    PID: _PID | None = Field(
        default=None,
        title="PID",
        description="Optional",
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
