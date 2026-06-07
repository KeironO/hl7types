"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RSP_K22
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
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.RSP_K22_QUERY_RESPONSE import RSP_K22_QUERY_RESPONSE

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RSP_K22_QUERY_RESPONSE = RSP_K22_QUERY_RESPONSE
_SFT = SFT
_UAC = UAC


class RSP_K22(HL7Model):
    """HL7 v2 RSP_K22 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (QAK): required
        QPD (QPD): required
        QUERY_RESPONSE (Optional[List[RSP_K22_QUERY_RESPONSE]]): optional
        DSC (Optional[DSC]): optional
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

    QUERY_RESPONSE: Optional[List[_RSP_K22_QUERY_RESPONSE]] = Field(
        default=None,
        title="QUERY_RESPONSE",
        description="Optional, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
