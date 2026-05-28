"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RTB_Z74
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RTB_Z74_ROW_DEFINITION import RTB_Z74_ROW_DEFINITION
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QPD import QPD

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RTB_Z74_ROW_DEFINITION = RTB_Z74_ROW_DEFINITION


class RTB_Z74(BaseModel):
    """HL7 v2 RTB_Z74 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (QAK): required
        QPD (QPD): required
        ROW_DEFINITION (Optional[RTB_Z74_ROW_DEFINITION]): optional
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

    ERR: _ERR | None = Field(
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

    ROW_DEFINITION: _RTB_Z74_ROW_DEFINITION | None = Field(
        default=None,
        title="ROW_DEFINITION",
        description="Optional",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
