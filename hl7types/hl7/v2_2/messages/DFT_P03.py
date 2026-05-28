"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: DFT_P03
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.FT1 import FT1
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_EVN = EVN
_FT1 = FT1
_MSH = MSH
_OBX = OBX
_PID = PID
_PV1 = PV1
_PV2 = PV2


class DFT_P03(BaseModel):
    """HL7 v2 DFT_P03 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        PV1 (Optional[PV1]): optional
        PV2 (Optional[PV2]): optional
        OBX (Optional[List[OBX]]): optional
        FT1 (List[FT1]): required
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

    PV2: _PV2 | None = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    FT1: list[_FT1] = Field(
        default=...,
        title="FT1",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
