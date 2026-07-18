"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NMQ_N02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH

from ..groups.NMQ_N02_CLOCK_AND_STATISTICS import NMQ_N02_CLOCK_AND_STATISTICS
from ..groups.NMQ_N02_QRY_WITH_DETAIL import NMQ_N02_QRY_WITH_DETAIL

_MSH = MSH
_NMQ_N02_CLOCK_AND_STATISTICS = NMQ_N02_CLOCK_AND_STATISTICS
_NMQ_N02_QRY_WITH_DETAIL = NMQ_N02_QRY_WITH_DETAIL


class NMQ_N02(HL7Model):
    """HL7 v2 NMQ_N02 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        QRY_WITH_DETAIL (Optional[NMQ_N02_QRY_WITH_DETAIL]): optional
        CLOCK_AND_STATISTICS (List[NMQ_N02_CLOCK_AND_STATISTICS]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    QRY_WITH_DETAIL: Optional[_NMQ_N02_QRY_WITH_DETAIL] = Field(
        default=None,
        title="QRY_WITH_DETAIL",
    )

    CLOCK_AND_STATISTICS: List[_NMQ_N02_CLOCK_AND_STATISTICS] = Field(
        min_length=1,
        title="CLOCK_AND_STATISTICS",
    )

    model_config = ConfigDict(populate_by_name=True)
