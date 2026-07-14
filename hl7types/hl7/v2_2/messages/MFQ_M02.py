"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFQ_M02
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_DSC = DSC
_MSH = MSH
_QRD = QRD
_QRF = QRF


class MFQ_M02(HL7Model):
    """HL7 v2 MFQ_M02 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        QRD (QRD): QUERY DEFINITION, required
        QRF (Optional[QRF]): QUERY FILTER, optional
        DSC (Optional[DSC]): CONTINUATION POINTER, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="QUERY DEFINITION",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="QUERY FILTER",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="CONTINUATION POINTER",
    )

    model_config = {"populate_by_name": True}
