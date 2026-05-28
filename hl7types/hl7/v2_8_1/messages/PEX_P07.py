"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PEX_P07
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.PEX_P07_EXPERIENCE import PEX_P07_EXPERIENCE
from ..groups.PEX_P07_VISIT import PEX_P07_VISIT
from ..segments.ARV import ARV
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_ARV = ARV
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


class PEX_P07(BaseModel):
    """HL7 v2 PEX_P07 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        NTE (Optional[List[NTE]]): optional
        VISIT (Optional[PEX_P07_VISIT]): optional
        EXPERIENCE (List[PEX_P07_EXPERIENCE]): required
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

    PD1: _PD1 | None = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VISIT: _PEX_P07_VISIT | None = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    EXPERIENCE: list[_PEX_P07_EXPERIENCE] = Field(
        default=...,
        title="EXPERIENCE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
