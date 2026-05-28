"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z90
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RSP_Z90_QUERY_RESPONSE import RSP_Z90_QUERY_RESPONSE
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QPD import QPD
from ..segments.RCP import RCP

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RCP = RCP
_RSP_Z90_QUERY_RESPONSE = RSP_Z90_QUERY_RESPONSE


class RSP_Z90(BaseModel):
    """HL7 v2 RSP_Z90 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (QAK): required
        QPD (QPD): required
        RCP (RCP): required
        QUERY_RESPONSE (List[RSP_Z90_QUERY_RESPONSE]): required
        DSC (DSC): required
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

    RCP: _RCP = Field(
        default=...,
        title="RCP",
        description="Required",
    )

    QUERY_RESPONSE: list[_RSP_Z90_QUERY_RESPONSE] = Field(
        default=...,
        title="QUERY_RESPONSE",
        description="Required, repeating",
    )

    DSC: _DSC = Field(
        default=...,
        title="DSC",
        description="Required",
    )

    model_config = {"populate_by_name": True}
