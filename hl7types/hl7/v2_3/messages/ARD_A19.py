"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ARD_A19
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
from ..segments.QRD import QRD
from ..segments.QRF import QRF

from ..groups.ARD_A19_QUERY_RESPONSE import ARD_A19_QUERY_RESPONSE

_ARD_A19_QUERY_RESPONSE = ARD_A19_QUERY_RESPONSE
_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QRD = QRD
_QRF = QRF


class ARD_A19(HL7Model):
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
        title="MSH",
        description="Required",
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

    QRD: _QRD = Field(
        title="QRD",
        description="Required",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    QUERY_RESPONSE: List[_ARD_A19_QUERY_RESPONSE] = Field(
        min_length=1,
        title="QUERY_RESPONSE",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
