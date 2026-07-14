"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NMR_N02
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

from ..groups.NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT import NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT = NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT
_QRD = QRD


class NMR_N02(HL7Model):
    """HL7 v2 NMR_N02 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        MSA (MSA): MESSAGE ACKNOWLEDGMENT, required
        ERR (Optional[ERR]): ERROR, optional
        QRD (Optional[QRD]): QUERY DEFINITION, optional
        CLOCK_AND_STATS_WITH_NOTES_ALT (List[NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MESSAGE ACKNOWLEDGMENT",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="ERROR",
    )

    QRD: Optional[_QRD] = Field(
        default=None,
        title="QRD",
        description="QUERY DEFINITION",
    )

    CLOCK_AND_STATS_WITH_NOTES_ALT: List[_NMR_N02_CLOCK_AND_STATS_WITH_NOTES_ALT] = Field(
        min_length=1,
        title="CLOCK_AND_STATS_WITH_NOTES_ALT",
    )

    model_config = {"populate_by_name": True}
