"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
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
from ..segments.PRT import PRT
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.PEX_P07_EXPERIENCE import PEX_P07_EXPERIENCE
from ..groups.PEX_P07_VISIT import PEX_P07_VISIT

_EVN = EVN
_MSH = MSH
_NTE = NTE
_PD1 = PD1
_PEX_P07_EXPERIENCE = PEX_P07_EXPERIENCE
_PEX_P07_VISIT = PEX_P07_VISIT
_PID = PID
_PRT = PRT
_SFT = SFT
_UAC = UAC


class PEX_P07(HL7Model):
    """PEX - Unsolicited initial individual product experience report (S7.11.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VISIT (Optional[PEX_P07_VISIT]): optional
        EXPERIENCE (List[PEX_P07_EXPERIENCE]): required
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

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Additional Demographic",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
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
