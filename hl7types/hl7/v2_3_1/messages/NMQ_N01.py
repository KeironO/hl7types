"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: NMQ_N01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH

from ..groups.NMQ_N01_CLOCK_AND_STATISTICS import NMQ_N01_CLOCK_AND_STATISTICS
from ..groups.NMQ_N01_QRY_WITH_DETAIL import NMQ_N01_QRY_WITH_DETAIL

_MSH = MSH
_NMQ_N01_CLOCK_AND_STATISTICS = NMQ_N01_CLOCK_AND_STATISTICS
_NMQ_N01_QRY_WITH_DETAIL = NMQ_N01_QRY_WITH_DETAIL


class NMQ_N01(HL7Model):
    """NMQ/NMR - Application management query message.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        QRY_WITH_DETAIL (Optional[NMQ_N01_QRY_WITH_DETAIL]): optional
        CLOCK_AND_STATISTICS (List[NMQ_N01_CLOCK_AND_STATISTICS]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    QRY_WITH_DETAIL: Optional[_NMQ_N01_QRY_WITH_DETAIL] = Field(
        default=None,
        title="QRY_WITH_DETAIL",
    )

    CLOCK_AND_STATISTICS: List[_NMQ_N01_CLOCK_AND_STATISTICS] = Field(
        min_length=1,
        title="CLOCK_AND_STATISTICS",
    )

    model_config = ConfigDict(populate_by_name=True)
