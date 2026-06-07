"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_Z90
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QPD import QPD
from ..segments.RCP import RCP
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.RSP_Z90_QUERY_RESPONSE import RSP_Z90_QUERY_RESPONSE

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RCP = RCP
_RSP_Z90_QUERY_RESPONSE = RSP_Z90_QUERY_RESPONSE
_SFT = SFT
_UAC = UAC


class RSP_Z90(HL7Model):
    """HL7 v2 RSP_Z90 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (QAK): required
        QPD (QPD): required
        RCP (RCP): required
        QUERY_RESPONSE (List[RSP_Z90_QUERY_RESPONSE]): required
        DSC (DSC): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
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

    RCP: _RCP = Field(
        title="RCP",
        description="Required",
    )

    QUERY_RESPONSE: List[_RSP_Z90_QUERY_RESPONSE] = Field(
        min_length=1,
        title="QUERY_RESPONSE",
        description="Required, repeating",
    )

    DSC: _DSC = Field(
        title="DSC",
        description="Required",
    )

    model_config = {"populate_by_name": True}
