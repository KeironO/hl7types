"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: NMD_N02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.NMD_N02_CLOCK_AND_STATS_WITH_NOTES import NMD_N02_CLOCK_AND_STATS_WITH_NOTES
from ..segments.MSH import MSH
from ..segments.SFT import SFT

_MSH = MSH
_NMD_N02_CLOCK_AND_STATS_WITH_NOTES = NMD_N02_CLOCK_AND_STATS_WITH_NOTES
_SFT = SFT


class NMD_N02(BaseModel):
    """HL7 v2 NMD_N02 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        CLOCK_AND_STATS_WITH_NOTES (List[NMD_N02_CLOCK_AND_STATS_WITH_NOTES]): required
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

    CLOCK_AND_STATS_WITH_NOTES: list[_NMD_N02_CLOCK_AND_STATS_WITH_NOTES] = Field(
        default=...,
        title="CLOCK_AND_STATS_WITH_NOTES",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
