"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QCN_J01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.QID import QID
from ..segments.SFT import SFT

_MSH = MSH
_QID = QID
_SFT = SFT


class QCN_J01(BaseModel):
    """HL7 v2 QCN_J01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        QID (QID): required
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

    QID: _QID = Field(
        default=...,
        title="QID",
        description="Required",
    )

    model_config = {"populate_by_name": True}
