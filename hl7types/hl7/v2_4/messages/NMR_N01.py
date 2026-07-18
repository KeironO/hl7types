"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: NMR_N01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
    """NMQ/NMR - Application management query message (S14).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QRD (Optional[QRD]): Original-Style Query Definition, optional
        CLOCK_AND_STATS_WITH_NOTES_ALT (List[NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    QRD: Optional[_QRD] = Field(
        default=None,
        title="QRD",
        description="Original-Style Query Definition",
    )

    CLOCK_AND_STATS_WITH_NOTES_ALT: List[_NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT] = Field(
        min_length=1,
        title="CLOCK_AND_STATS_WITH_NOTES_ALT",
    )

    model_config = ConfigDict(populate_by_name=True)
