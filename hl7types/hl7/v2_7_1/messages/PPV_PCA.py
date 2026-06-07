"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PPV_PCA
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.PPV_PCA_PATIENT import PPV_PCA_PATIENT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PPV_PCA_PATIENT = PPV_PCA_PATIENT
_QAK = QAK
_QRD = QRD
_SFT = SFT
_UAC = UAC


class PPV_PCA(HL7Model):
    """HL7 v2 PPV_PCA message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        QAK (Optional[QAK]): optional
        QRD (QRD): required
        PATIENT (List[PPV_PCA_PATIENT]): required
    """

    MSH: _MSH = Field(
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
        title="QRD",
        description="Required",
    )

    PATIENT: List[_PPV_PCA_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
