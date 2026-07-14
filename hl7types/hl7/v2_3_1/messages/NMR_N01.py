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
    """NMQ/NMR - Application management query message.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        ERR (Optional[List[ERR]]): ERR - error segment, optional
        QRD (Optional[QRD]): QRD - original-style query definition segment, optional
        CLOCK_AND_STATS_WITH_NOTES_ALT (List[NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MSA - message acknowledgment segment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="ERR - error segment",
    )

    QRD: Optional[_QRD] = Field(
        default=None,
        title="QRD",
        description="QRD - original-style query definition segment",
    )

    CLOCK_AND_STATS_WITH_NOTES_ALT: List[_NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT] = Field(
        min_length=1,
        title="CLOCK_AND_STATS_WITH_NOTES_ALT",
    )

    model_config = {"populate_by_name": True}
