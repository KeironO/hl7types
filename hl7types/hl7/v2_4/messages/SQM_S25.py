"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SQM_S25
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

from ..groups.SQM_S25_REQUEST import SQM_S25_REQUEST

_DSC = DSC
_MSH = MSH
_QRD = QRD
_QRF = QRF
_SQM_S25_REQUEST = SQM_S25_REQUEST


class SQM_S25(HL7Model):
    """SQM/SQR - Schedule query message and response (S10).

    Attributes:
        MSH (MSH): Message Header, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        REQUEST (Optional[SQM_S25_REQUEST]): optional
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

    REQUEST: Optional[_SQM_S25_REQUEST] = Field(
        default=None,
        title="REQUEST",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
