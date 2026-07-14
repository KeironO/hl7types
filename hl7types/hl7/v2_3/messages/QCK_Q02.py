"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: QCK_Q02
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
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
    """QRY/ACK - Query sent for deferred response.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        ERR (Optional[ERR]): Error segment, optional
        QAK (Optional[QAK]): Query Acknowledgement, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message acknowledgement segment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error segment",
    )

    QAK: Optional[_QAK] = Field(
        default=None,
        title="QAK",
        description="Query Acknowledgement",
    )

    model_config = {"populate_by_name": True}
