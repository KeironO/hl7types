"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: DSR_R03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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


class DSR_R03(HL7Model):
    """HL7 v2 DSR_R03 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        MSA (Optional[MSA]): MESSAGE ACKNOWLEDGMENT, optional
        QRD (QRD): QUERY DEFINITION, required
        QRF (Optional[QRF]): QUERY FILTER, optional
        DSP (List[DSP]): DISPLAY DATA, required
        DSC (Optional[DSC]): CONTINUATION POINTER, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    MSA: Optional[_MSA] = Field(
        default=None,
        title="MSA",
        description="MESSAGE ACKNOWLEDGMENT",
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

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="CONTINUATION POINTER",
    )

    model_config = ConfigDict(populate_by_name=True)
