"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
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
from ..segments.SFT import SFT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT = NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT
_QRD = QRD
_SFT = SFT


class NMR_N01(BaseModel):
    """HL7 v2 NMR_N01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        QRD (Optional[QRD]): optional
        CLOCK_AND_STATS_WITH_NOTES_ALT (List[NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT]): required
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

    ERR: list[_ERR] | None = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
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
