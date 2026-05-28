"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: NMQ_N01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.NMQ_N01_CLOCK_AND_STATISTICS import NMQ_N01_CLOCK_AND_STATISTICS
from ..groups.NMQ_N01_QRY_WITH_DETAIL import NMQ_N01_QRY_WITH_DETAIL
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_NMQ_N01_CLOCK_AND_STATISTICS = NMQ_N01_CLOCK_AND_STATISTICS
_NMQ_N01_QRY_WITH_DETAIL = NMQ_N01_QRY_WITH_DETAIL
_SFT = SFT
_UAC = UAC


class NMQ_N01(BaseModel):
    """HL7 v2 NMQ_N01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        QRY_WITH_DETAIL (Optional[NMQ_N01_QRY_WITH_DETAIL]): optional
        CLOCK_AND_STATISTICS (List[NMQ_N01_CLOCK_AND_STATISTICS]): required
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

    QRY_WITH_DETAIL: _NMQ_N01_QRY_WITH_DETAIL | None = Field(
        default=None,
        title="QRY_WITH_DETAIL",
        description="Optional",
    )

    CLOCK_AND_STATISTICS: list[_NMQ_N01_CLOCK_AND_STATISTICS] = Field(
        default=...,
        title="CLOCK_AND_STATISTICS",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
