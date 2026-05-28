"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RSP_Q11
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RSP_Q11_QUERY_RESULT_CLUSTER import RSP_Q11_QUERY_RESULT_CLUSTER
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QPD import QPD
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RSP_Q11_QUERY_RESULT_CLUSTER = RSP_Q11_QUERY_RESULT_CLUSTER
_SFT = SFT
_UAC = UAC


class RSP_Q11(BaseModel):
    """HL7 v2 RSP_Q11 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        QAK (QAK): required
        QPD (QPD): required
        QUERY_RESULT_CLUSTER (Optional[RSP_Q11_QUERY_RESULT_CLUSTER]): optional
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: list[_ERR] | None = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
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

    QUERY_RESULT_CLUSTER: _RSP_Q11_QUERY_RESULT_CLUSTER | None = Field(
        default=None,
        title="QUERY_RESULT_CLUSTER",
        description="Optional",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
