"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QCN_J01
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.QID import QID

_MSH = MSH
_QID = QID


class QCN_J01(BaseModel):
    """HL7 v2 QCN_J01 message.

    Attributes:
        MSH (MSH): required
        QID (QID): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    QID: _QID = Field(
        default=...,
        title="QID",
        description="Required",
    )

    model_config = {"populate_by_name": True}
