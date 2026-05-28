"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ADT_A37
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DB1 import DB1
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DB1 = DB1
_EVN = EVN
_MSH = MSH
_PD1 = PD1
_PID = PID
_PV1 = PV1
_SFT = SFT
_UAC = UAC


class ADT_A37(BaseModel):
    """HL7 v2 ADT_A37 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PV1 (Optional[PV1]): optional
        DB1 (Optional[List[DB1]]): optional
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

    PV1: _PV1 | None = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    DB1: list[_DB1] | None = Field(
        default=None,
        title="DB1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
