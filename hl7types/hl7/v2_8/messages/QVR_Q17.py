"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: QVR_Q17
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.QVR_Q17_QBP import QVR_Q17_QBP
from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.RCP import RCP
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DSC = DSC
_MSH = MSH
_QPD = QPD
_QVR_Q17_QBP = QVR_Q17_QBP
_RCP = RCP
_SFT = SFT
_UAC = UAC


class QVR_Q17(BaseModel):
    """HL7 v2 QVR_Q17 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        QPD (QPD): required
        QBP (Optional[QVR_Q17_QBP]): optional
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

    QBP: _QVR_Q17_QBP | None = Field(
        default=None,
        title="QBP",
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
