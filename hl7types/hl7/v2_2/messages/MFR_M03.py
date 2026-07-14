"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFR_M03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MFI import MFI
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

from ..groups.MFR_M03_MF_TEST import MFR_M03_MF_TEST

_DSC = DSC
_ERR = ERR
_MFI = MFI
_MFR_M03_MF_TEST = MFR_M03_MF_TEST
_MSA = MSA
_MSH = MSH
_QRD = QRD
_QRF = QRF


class MFR_M03(HL7Model):
    """HL7 v2 MFR_M03 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        MSA (MSA): MESSAGE ACKNOWLEDGMENT, required
        ERR (Optional[ERR]): ERROR, optional
        QRD (QRD): QUERY DEFINITION, required
        QRF (Optional[QRF]): QUERY FILTER, optional
        MFI (MFI): MASTER FILE IDENTIFICATION, required
        MF_TEST (List[MFR_M03_MF_TEST]): required
        DSC (Optional[DSC]): CONTINUATION POINTER, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MESSAGE ACKNOWLEDGMENT",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="ERROR",
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

    MFI: _MFI = Field(
        title="MFI",
        description="MASTER FILE IDENTIFICATION",
    )

    MF_TEST: List[_MFR_M03_MF_TEST] = Field(
        min_length=1,
        title="MF_TEST",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="CONTINUATION POINTER",
    )

    model_config = {"populate_by_name": True}
