"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PPT_PCL
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.PPT_PCL_PATIENT import PPT_PCL_PATIENT
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PPT_PCL_PATIENT = PPT_PCL_PATIENT
_QRD = QRD


class PPT_PCL(BaseModel):
    """HL7 v2 PPT_PCL message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QRD (QRD): required
        PATIENT (List[PPT_PCL_PATIENT]): required
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

    ERR: _ERR | None = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    PATIENT: list[_PPT_PCL_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
