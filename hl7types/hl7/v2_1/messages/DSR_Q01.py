"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: DSR_Q01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.DSP import DSP
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_DSC = DSC
_DSP = DSP
_MSA = MSA
_MSH = MSH
_QRD = QRD
_QRF = QRF


class DSR_Q01(HL7Model):
    """HL7 v2 DSR_Q01 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        DSP (List[DSP]): required
        DSC (DSC): required
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

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    DSP: List[_DSP] = Field(
        default=...,
        title="DSP",
        description="Required, repeating",
    )

    DSC: _DSC = Field(
        default=...,
        title="DSC",
        description="Required",
    )

    model_config = {"populate_by_name": True}
