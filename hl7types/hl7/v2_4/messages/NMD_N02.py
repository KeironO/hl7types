"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: NMD_N02
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH

from ..groups.NMD_N02_CLOCK_AND_STATS_WITH_NOTES import NMD_N02_CLOCK_AND_STATS_WITH_NOTES

_MSH = MSH
_NMD_N02_CLOCK_AND_STATS_WITH_NOTES = NMD_N02_CLOCK_AND_STATS_WITH_NOTES


class NMD_N02(HL7Model):
    """NMD/ACK - Application management data message (unsolicited) (S14).

    Attributes:
        MSH (MSH): Message Header, required
        CLOCK_AND_STATS_WITH_NOTES (List[NMD_N02_CLOCK_AND_STATS_WITH_NOTES]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    CLOCK_AND_STATS_WITH_NOTES: List[_NMD_N02_CLOCK_AND_STATS_WITH_NOTES] = Field(
        min_length=1,
        title="CLOCK_AND_STATS_WITH_NOTES",
    )

    model_config = ConfigDict(populate_by_name=True)
