"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PTR_PCF
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD

from ..groups.PTR_PCF_PATIENT import PTR_PCF_PATIENT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PTR_PCF_PATIENT = PTR_PCF_PATIENT
_QRD = QRD


class PTR_PCF(HL7Model):
    """PPP - PC/Pathway (Problem Oriented) Query Response.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        ERR (Optional[ERR]): Error segment, optional
        QRD (QRD): Query definition segment, required
        PATIENT (List[PTR_PCF_PATIENT]): required
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

    QRD: _QRD = Field(
        title="QRD",
        description="Query definition segment",
    )

    PATIENT: List[_PTR_PCF_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)
