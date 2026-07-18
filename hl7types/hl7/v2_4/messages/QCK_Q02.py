"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QCK_Q02
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK

_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK


class QCK_Q02(HL7Model):
    """QRY/QCK - Query sent for deferred response (S5).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (Optional[QAK]): Query Acknowledgment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    QAK: Optional[_QAK] = Field(
        default=None,
        title="QAK",
        description="Query Acknowledgment",
    )

    model_config = ConfigDict(populate_by_name=True)
