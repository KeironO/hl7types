"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: NMD_N02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.NMD_N02_CLOCK_AND_STATS_WITH_NOTES import NMD_N02_CLOCK_AND_STATS_WITH_NOTES

_MSH = MSH
_NMD_N02_CLOCK_AND_STATS_WITH_NOTES = NMD_N02_CLOCK_AND_STATS_WITH_NOTES
_SFT = SFT
_UAC = UAC


class NMD_N02(HL7Model):
    """NMD/ACK - Application management data message (unsolicited) (S14.3.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        CLOCK_AND_STATS_WITH_NOTES (List[NMD_N02_CLOCK_AND_STATS_WITH_NOTES]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    CLOCK_AND_STATS_WITH_NOTES: List[_NMD_N02_CLOCK_AND_STATS_WITH_NOTES] = Field(
        min_length=1,
        title="CLOCK_AND_STATS_WITH_NOTES",
    )

    model_config = {"populate_by_name": True}
