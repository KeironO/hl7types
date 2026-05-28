"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QCK_Q02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK

_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK


class QCK_Q02(BaseModel):
    """HL7 v2 QCK_Q02 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (Optional[QAK]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: _ERR | None = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    QAK: _QAK | None = Field(
        default=None,
        title="QAK",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
