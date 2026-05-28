"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: DFT_P03
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.FT1 import FT1
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1

_EVN = EVN
_FT1 = FT1
_MSH = MSH
_PID = PID
_PV1 = PV1


class DFT_P03(BaseModel):
    """HL7 v2 DFT_P03 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        PV1 (Optional[PV1]): optional
        FT1 (Optional[List[FT1]]): optional
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

    PV1: _PV1 | None = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    FT1: list[_FT1] | None = Field(
        default=None,
        title="FT1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
