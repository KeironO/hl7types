"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_K11
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RSP_K11_SEGMENT_PATTERN import RSP_K11_SEGMENT_PATTERN
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QPD import QPD
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QPD = QPD
_RSP_K11_SEGMENT_PATTERN = RSP_K11_SEGMENT_PATTERN
_SFT = SFT
_UAC = UAC


class RSP_K11(BaseModel):
    """HL7 v2 RSP_K11 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (QAK): required
        QPD (QPD): required
        SEGMENT_PATTERN (Optional[RSP_K11_SEGMENT_PATTERN]): optional
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

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
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

    SEGMENT_PATTERN: _RSP_K11_SEGMENT_PATTERN | None = Field(
        default=None,
        title="SEGMENT_PATTERN",
        description="Optional",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
