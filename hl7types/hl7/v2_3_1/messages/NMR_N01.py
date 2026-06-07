"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: NMR_N01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD

from ..groups.NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT import NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT = NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT
_QRD = QRD


class NMR_N01(HL7Model):
    """HL7 v2 NMR_N01 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        QRD (Optional[QRD]): optional
        CLOCK_AND_STATS_WITH_NOTES_ALT (List[NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
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

    QRD: Optional[_QRD] = Field(
        default=None,
        title="QRD",
        description="Optional",
    )

    CLOCK_AND_STATS_WITH_NOTES_ALT: List[_NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT] = Field(
        min_length=1,
        title="CLOCK_AND_STATS_WITH_NOTES_ALT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
