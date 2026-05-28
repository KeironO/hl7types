"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PPT_PCL
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.PPT_PCL_PATIENT import PPT_PCL_PATIENT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PPT_PCL_PATIENT = PPT_PCL_PATIENT
_QAK = QAK
_QRD = QRD
_SFT = SFT
_UAC = UAC


class PPT_PCL(BaseModel):
    """HL7 v2 PPT_PCL message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        QAK (Optional[QAK]): optional
        QRD (QRD): required
        PATIENT (List[PPT_PCL_PATIENT]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    QAK: Optional[_QAK] = Field(
        default=None,
        title="QAK",
        description="Optional",
    )

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    PATIENT: List[_PPT_PCL_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
