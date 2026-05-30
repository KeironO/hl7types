"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_K13
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

from ..groups.RSP_K13_ROW_DEFINITION import RSP_K13_ROW_DEFINITION

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RSP_K13_ROW_DEFINITION = RSP_K13_ROW_DEFINITION


class RSP_K13(HL7Model):
    """HL7 v2 RSP_K13 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (QAK): required
        QPD (QPD): required
        ROW_DEFINITION (Optional[RSP_K13_ROW_DEFINITION]): optional
        DSC (Optional[DSC]): optional
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

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    QAK: _QAK = Field(
        default=...,
        title="QAK",
        description="Required",
    )

    QPD: _QPD = Field(
        default=...,
        title="QPD",
        description="Required",
    )

    ROW_DEFINITION: Optional[_RSP_K13_ROW_DEFINITION] = Field(
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
