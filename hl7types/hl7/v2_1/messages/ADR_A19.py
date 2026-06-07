"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADR_A19
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD

from ..groups.ADR_A19_QUERY_RESPONSE import ADR_A19_QUERY_RESPONSE

_ADR_A19_QUERY_RESPONSE = ADR_A19_QUERY_RESPONSE
_DSC = DSC
_MSA = MSA
_MSH = MSH
_QRD = QRD


class ADR_A19(HL7Model):
    """HL7 v2 ADR_A19 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        QRD (QRD): required
        QUERY_RESPONSE (List[ADR_A19_QUERY_RESPONSE]): required
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

    QRD: _QRD = Field(
        title="QRD",
        description="Required",
    )

    QUERY_RESPONSE: List[_ADR_A19_QUERY_RESPONSE] = Field(
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
