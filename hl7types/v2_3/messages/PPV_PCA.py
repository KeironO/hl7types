"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PPV_PCA
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD

from ..groups.PPV_PCA_PATIENT import PPV_PCA_PATIENT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PPV_PCA_PATIENT = PPV_PCA_PATIENT
_QRD = QRD


class PPV_PCA(BaseModel):
    """HL7 v2 PPV_PCA message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QRD (QRD): required
        PATIENT (List[PPV_PCA_PATIENT]): required
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

    PATIENT: List[_PPV_PCA_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
