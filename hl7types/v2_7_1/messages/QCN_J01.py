"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: QCN_J01
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.QID import QID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_QID = QID
_SFT = SFT
_UAC = UAC


class QCN_J01(BaseModel):
    """HL7 v2 QCN_J01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        QID (QID): required
    """

    MSH: _MSH = Field(
        default=...,
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

    QID: _QID = Field(
        default=...,
        title="QID",
        description="Required",
    )

    model_config = {"populate_by_name": True}
