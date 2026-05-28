"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: DOC_T12
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.DOC_T12_RESULT import DOC_T12_RESULT
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD

_DOC_T12_RESULT = DOC_T12_RESULT
_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QRD = QRD


class DOC_T12(BaseModel):
    """HL7 v2 DOC_T12 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QRD (QRD): required
        RESULT (List[DOC_T12_RESULT]): required
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

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    RESULT: list[_DOC_T12_RESULT] = Field(
        default=...,
        title="RESULT",
        description="Required, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
