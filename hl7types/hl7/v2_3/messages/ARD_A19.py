"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ARD_A19
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ARD_A19_QUERY_RESPONSE import ARD_A19_QUERY_RESPONSE
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_ARD_A19_QUERY_RESPONSE = ARD_A19_QUERY_RESPONSE
_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QRD = QRD
_QRF = QRF


class ARD_A19(BaseModel):
    """HL7 v2 ARD_A19 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        QUERY_RESPONSE (List[ARD_A19_QUERY_RESPONSE]): required
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

    QRF: _QRF | None = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    QUERY_RESPONSE: list[_ARD_A19_QUERY_RESPONSE] = Field(
        default=...,
        title="QUERY_RESPONSE",
        description="Required, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
