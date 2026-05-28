"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_K31
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RSP_K31_RESPONSE import RSP_K31_RESPONSE
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QPD import QPD
from ..segments.RCP import RCP
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RCP = RCP
_RSP_K31_RESPONSE = RSP_K31_RESPONSE
_SFT = SFT
_UAC = UAC


class RSP_K31(BaseModel):
    """HL7 v2 RSP_K31 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        QAK (QAK): required
        QPD (QPD): required
        RCP (RCP): required
        RESPONSE (List[RSP_K31_RESPONSE]): required
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

    ERR: list[_ERR] | None = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
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

    RESPONSE: list[_RSP_K31_RESPONSE] = Field(
        default=...,
        title="RESPONSE",
        description="Required, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
