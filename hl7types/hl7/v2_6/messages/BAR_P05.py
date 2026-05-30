"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: BAR_P05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.BAR_P05_VISIT import BAR_P05_VISIT

_BAR_P05_VISIT = BAR_P05_VISIT
_EVN = EVN
_MSH = MSH
_PD1 = PD1
_PID = PID
_ROL = ROL
_SFT = SFT
_UAC = UAC


class BAR_P05(HL7Model):
    """HL7 v2 BAR_P05 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        ROL (Optional[List[ROL]]): optional
        VISIT (List[BAR_P05_VISIT]): required
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

    UAC: Optional[_UAC] = Field(
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

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    VISIT: List[_BAR_P05_VISIT] = Field(
        default=...,
        title="VISIT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
