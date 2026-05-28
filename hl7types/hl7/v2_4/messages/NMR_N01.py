"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: NMR_N01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT import NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT = NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT
_QRD = QRD


class NMR_N01(BaseModel):
    """HL7 v2 NMR_N01 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QRD (Optional[QRD]): optional
        CLOCK_AND_STATS_WITH_NOTES_ALT (List[NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT]): required
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

    QRD: _QRD | None = Field(
        default=None,
        title="QRD",
        description="Optional",
    )

    CLOCK_AND_STATS_WITH_NOTES_ALT: list[_NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT] = Field(
        default=...,
        title="CLOCK_AND_STATS_WITH_NOTES_ALT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
