"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ADR_A19
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD

from ..groups.ADR_A19_QUERY_RESPONSE import ADR_A19_QUERY_RESPONSE

_ADR_A19_QUERY_RESPONSE = ADR_A19_QUERY_RESPONSE
_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QRD = QRD


class ADR_A19(HL7Model):
    """HL7 v2 ADR_A19 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        MSA (MSA): MESSAGE ACKNOWLEDGMENT, required
        ERR (Optional[ERR]): ERROR, optional
        QRD (QRD): QUERY DEFINITION, required
        QUERY_RESPONSE (List[ADR_A19_QUERY_RESPONSE]): required
        DSC (Optional[DSC]): CONTINUATION POINTER, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MESSAGE ACKNOWLEDGMENT",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="ERROR",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="QUERY DEFINITION",
    )

    QUERY_RESPONSE: List[_ADR_A19_QUERY_RESPONSE] = Field(
        min_length=1,
        title="QUERY_RESPONSE",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="CONTINUATION POINTER",
    )

    model_config = ConfigDict(populate_by_name=True)
