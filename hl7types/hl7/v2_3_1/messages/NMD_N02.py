"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: NMD_N02
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH

from ..groups.NMD_N02_CLOCK_AND_STATS_WITH_NOTES import NMD_N02_CLOCK_AND_STATS_WITH_NOTES

_MSH = MSH
_NMD_N02_CLOCK_AND_STATS_WITH_NOTES = NMD_N02_CLOCK_AND_STATS_WITH_NOTES


class NMD_N02(HL7Model):
    """HL7 v2 NMD_N02 message.

    Attributes:
        MSH (MSH): required
        CLOCK_AND_STATS_WITH_NOTES (List[NMD_N02_CLOCK_AND_STATS_WITH_NOTES]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    CLOCK_AND_STATS_WITH_NOTES: List[_NMD_N02_CLOCK_AND_STATS_WITH_NOTES] = Field(
        min_length=1,
        title="CLOCK_AND_STATS_WITH_NOTES",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
