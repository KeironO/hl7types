"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: BAR_P01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.BAR_P01_VISIT import BAR_P01_VISIT
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_BAR_P01_VISIT = BAR_P01_VISIT
_EVN = EVN
_MSH = MSH
_PD1 = PD1
_PID = PID
_PRT = PRT
_ROL = ROL
_SFT = SFT
_UAC = UAC


class BAR_P01(BaseModel):
    """HL7 v2 BAR_P01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
        VISIT (List[BAR_P01_VISIT]): required
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

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    VISIT: list[_BAR_P01_VISIT] = Field(
        default=...,
        title="VISIT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
