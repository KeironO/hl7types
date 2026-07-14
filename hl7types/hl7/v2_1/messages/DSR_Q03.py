"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: DSR_Q03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class DSR_Q03(HL7Model):
    """HL7 v2 DSR_Q03 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        QRD (QRD): QUERY DEFINITION, required
        QRF (Optional[QRF]): QUERY FILTER, optional
        DSP (List[DSP]): DISPLAY DATA, required
        DSC (DSC): CONTINUATION POINTER, required
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

    DSP: List[_DSP] = Field(
        min_length=1,
        title="DSP",
        description="DISPLAY DATA",
    )

    DSC: _DSC = Field(
        title="DSC",
        description="CONTINUATION POINTER",
    )

    model_config = {"populate_by_name": True}
