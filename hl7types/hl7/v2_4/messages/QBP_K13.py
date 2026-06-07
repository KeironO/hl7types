"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_K13
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QPD import QPD

from ..groups.QBP_K13_ROW_DEFINITION import QBP_K13_ROW_DEFINITION

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QBP_K13_ROW_DEFINITION = QBP_K13_ROW_DEFINITION
_QPD = QPD


class QBP_K13(HL7Model):
    """HL7 v2 QBP_K13 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (QAK): required
        QPD (QPD): required
        ROW_DEFINITION (Optional[QBP_K13_ROW_DEFINITION]): optional
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Required",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    QAK: _QAK = Field(
        title="QAK",
        description="Required",
    )

    QPD: _QPD = Field(
        title="QPD",
        description="Required",
    )

    ROW_DEFINITION: Optional[_QBP_K13_ROW_DEFINITION] = Field(
        default=None,
        title="ROW_DEFINITION",
        description="Optional",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
