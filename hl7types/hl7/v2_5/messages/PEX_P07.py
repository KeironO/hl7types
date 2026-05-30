"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
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
from ..segments.SFT import SFT

from ..groups.PEX_P07_EXPERIENCE import PEX_P07_EXPERIENCE
from ..groups.PEX_P07_VISIT import PEX_P07_VISIT

_EVN = EVN
_MSH = MSH
_NTE = NTE
_PD1 = PD1
_PEX_P07_EXPERIENCE = PEX_P07_EXPERIENCE
_PEX_P07_VISIT = PEX_P07_VISIT
_PID = PID
_SFT = SFT


class PEX_P07(HL7Model):
    """HL7 v2 PEX_P07 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        VISIT (Optional[PEX_P07_VISIT]): optional
        EXPERIENCE (List[PEX_P07_EXPERIENCE]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    EVN: _EVN = Field(
        default=...,
        title="EVN",
        description="Required",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VISIT: Optional[_PEX_P07_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    EXPERIENCE: List[_PEX_P07_EXPERIENCE] = Field(
        default=...,
        title="EXPERIENCE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
