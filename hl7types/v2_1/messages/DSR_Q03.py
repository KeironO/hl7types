"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: DSR_Q03
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.DSP import DSP
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_DSC = DSC
_DSP = DSP
_MSH = MSH
_QRD = QRD
_QRF = QRF


class DSR_Q03(BaseModel):
    """HL7 v2 DSR_Q03 message.

    Attributes:
        MSH (MSH): required
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
