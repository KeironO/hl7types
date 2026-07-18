"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OSR_Q06
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.QRD import QRD
from ..segments.QRF import QRF

from ..groups.OSR_Q06_RESPONSE import OSR_Q06_RESPONSE

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_OSR_Q06_RESPONSE = OSR_Q06_RESPONSE
_QRD = QRD
_QRF = QRF


class OSR_Q06(HL7Model):
    """OSQ/OSR - Query for order status.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        ERR (Optional[ERR]): Error segment, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        QRD (QRD): Query definition segment, required
        QRF (Optional[QRF]): Query filter segment, optional
        RESPONSE (Optional[OSR_Q06_RESPONSE]): optional
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Query definition segment",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Query filter segment",
    )

    RESPONSE: Optional[_OSR_Q06_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
