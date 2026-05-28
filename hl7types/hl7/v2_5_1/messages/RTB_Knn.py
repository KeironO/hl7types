"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RTB_Knn
Type: Message
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QPD import QPD
from ..segments.SFT import SFT

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_SFT = SFT


class RTB_Knn(BaseModel):
    """HL7 v2 RTB_Knn message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (QAK): required
        QPD (QPD): required
        anyhl7segment (Optional[Any]): optional
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
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

    QAK: _QAK = Field(
        default=...,
        title="QAK",
        description="Required",
    )

    QPD: _QPD = Field(
        default=...,
        title="QPD",
        description="Required",
    )

    anyhl7segment: Any | None = None

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
