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
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        MFI (MFI): required
        MF_TEST (List[MFR_M03_MF_TEST]): required
        DSC (Optional[DSC]): optional
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

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
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

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF_TEST: List[_MFR_M03_MF_TEST] = Field(
        default=...,
        title="MF_TEST",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
