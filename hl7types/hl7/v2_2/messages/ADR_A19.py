"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ADR_A19
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ADR_A19_QUERY_RESPONSE import ADR_A19_QUERY_RESPONSE
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD

_ADR_A19_QUERY_RESPONSE = ADR_A19_QUERY_RESPONSE
_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QRD = QRD


class ADR_A19(BaseModel):
    """HL7 v2 ADR_A19 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QRD (QRD): required
        QUERY_RESPONSE (List[ADR_A19_QUERY_RESPONSE]): required
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

    QUERY_RESPONSE: list[_ADR_A19_QUERY_RESPONSE] = Field(
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
