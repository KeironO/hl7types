"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: BAR_P01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.BAR_P01_VISIT import BAR_P01_VISIT
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PID import PID

_BAR_P01_VISIT = BAR_P01_VISIT
_EVN = EVN
_MSH = MSH
_PID = PID


class BAR_P01(BaseModel):
    """HL7 v2 BAR_P01 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        VISIT (List[BAR_P01_VISIT]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
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

    VISIT: list[_BAR_P01_VISIT] = Field(
        default=...,
        title="VISIT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
