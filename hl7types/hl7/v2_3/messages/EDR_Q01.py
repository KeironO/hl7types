"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: EDR_Q01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.DSP import DSP
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK

_DSC = DSC
_DSP = DSP
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK


class EDR_Q01(HL7Model):
    """QRY/DSR - Query sent for immediate response.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        ERR (Optional[ERR]): Error segment, optional
        QAK (QAK): Query Acknowledgement, required
        DSP (List[DSP]): Display data segment, required
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message acknowledgement segment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error segment",
    )

    QAK: _QAK = Field(
        title="QAK",
        description="Query Acknowledgement",
    )

    DSP: List[_DSP] = Field(
        min_length=1,
        title="DSP",
        description="Display data segment",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation pointer segment",
    )

    model_config = {"populate_by_name": True}
