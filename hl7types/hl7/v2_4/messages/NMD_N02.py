"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: NMD_N02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.NMD_N02_CLOCK_AND_STATS_WITH_NOTES import NMD_N02_CLOCK_AND_STATS_WITH_NOTES
from ..segments.MSH import MSH

_MSH = MSH
_NMD_N02_CLOCK_AND_STATS_WITH_NOTES = NMD_N02_CLOCK_AND_STATS_WITH_NOTES


class NMD_N02(BaseModel):
    """HL7 v2 NMD_N02 message.

    Attributes:
        MSH (MSH): required
        CLOCK_AND_STATS_WITH_NOTES (List[NMD_N02_CLOCK_AND_STATS_WITH_NOTES]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    CLOCK_AND_STATS_WITH_NOTES: list[_NMD_N02_CLOCK_AND_STATS_WITH_NOTES] = Field(
        default=...,
        title="CLOCK_AND_STATS_WITH_NOTES",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
