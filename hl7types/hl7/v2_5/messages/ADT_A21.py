"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ADT_A21
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DB1 import DB1
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.SFT import SFT

_DB1 = DB1
_EVN = EVN
_MSH = MSH
_OBX = OBX
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2
_SFT = SFT


class ADT_A21(BaseModel):
    """HL7 v2 ADT_A21 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        DB1 (Optional[List[DB1]]): optional
        OBX (Optional[List[OBX]]): optional
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

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    PV2: _PV2 | None = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    DB1: list[_DB1] | None = Field(
        default=None,
        title="DB1",
        description="Optional, repeating",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
