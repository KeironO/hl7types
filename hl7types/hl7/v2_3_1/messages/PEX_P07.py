"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PEX_P07
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from ..groups.PEX_P07_EXPERIENCE import PEX_P07_EXPERIENCE
from ..groups.PEX_P07_VISIT import PEX_P07_VISIT

_EVN = EVN
_MSH = MSH
_NTE = NTE
_PD1 = PD1
_PEX_P07_EXPERIENCE = PEX_P07_EXPERIENCE
_PEX_P07_VISIT = PEX_P07_VISIT
_PID = PID


class PEX_P07(HL7Model):
    """PEX - Unsolicited initial individual product experience report.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        VISIT (Optional[PEX_P07_VISIT]): optional
        EXPERIENCE (List[PEX_P07_EXPERIENCE]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="EVN - event type segment",
    )

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="PD1 - patient additional demographic segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    VISIT: Optional[_PEX_P07_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    EXPERIENCE: List[_PEX_P07_EXPERIENCE] = Field(
        min_length=1,
        title="EXPERIENCE",
    )

    model_config = {"populate_by_name": True}
