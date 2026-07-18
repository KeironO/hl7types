"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NMD_N01
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH

from ..groups.NMD_N01_CLOCK_AND_STATS_WITH_NOTES import NMD_N01_CLOCK_AND_STATS_WITH_NOTES

_MSH = MSH
_NMD_N01_CLOCK_AND_STATS_WITH_NOTES = NMD_N01_CLOCK_AND_STATS_WITH_NOTES


class NMD_N01(HL7Model):
    """HL7 v2 NMD_N01 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        CLOCK_AND_STATS_WITH_NOTES (List[NMD_N01_CLOCK_AND_STATS_WITH_NOTES]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    CLOCK_AND_STATS_WITH_NOTES: List[_NMD_N01_CLOCK_AND_STATS_WITH_NOTES] = Field(
        min_length=1,
        title="CLOCK_AND_STATS_WITH_NOTES",
    )

    model_config = ConfigDict(populate_by_name=True)
