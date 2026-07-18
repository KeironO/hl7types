"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_K23
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.QAK import QAK
from ..segments.QPD import QPD

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_PID = PID
_QAK = QAK
_QPD = QPD


class RSP_K23(HL7Model):
    """RSP - Get corresponding identifiers response (S15).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        PID (Optional[PID]): Patient identification, optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    QAK: _QAK = Field(
        title="QAK",
        description="Query Acknowledgment",
    )

    QPD: _QPD = Field(
        title="QPD",
        description="Query Parameter Definition",
    )

    PID: Optional[_PID] = Field(
        default=None,
        title="PID",
        description="Patient identification",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
