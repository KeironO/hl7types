"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QCK_Q02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.SFT import SFT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_SFT = SFT


class QCK_Q02(HL7Model):
    """HL7 v2 QCK_Q02 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (Optional[QAK]): optional
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

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    QAK: Optional[_QAK] = Field(
        default=None,
        title="QAK",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
