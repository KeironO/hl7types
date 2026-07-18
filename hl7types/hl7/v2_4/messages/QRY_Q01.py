"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QRY_Q01
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_DSC = DSC
_MSH = MSH
_QRD = QRD
_QRF = QRF


class QRY_Q01(HL7Model):
    """QRY/DSR - Query sent for immediate response (S12).

    Attributes:
        MSH (MSH): Message Header, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Original-Style Query Definition",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Original Style Query Filter",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
