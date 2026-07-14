"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OSR_Q06
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OSR_Q06_RESPONSE import OSR_Q06_RESPONSE

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_OSR_Q06_RESPONSE = OSR_Q06_RESPONSE
_QRD = QRD
_QRF = QRF
_SFT = SFT
_UAC = UAC


class OSR_Q06(HL7Model):
    """OSQ/OSR - Query for order status (S4.4.3).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original style query filter, optional
        RESPONSE (Optional[OSR_Q06_RESPONSE]): optional
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

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Original-Style Query Definition",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Original style query filter",
    )

    RESPONSE: Optional[_OSR_Q06_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = {"populate_by_name": True}
