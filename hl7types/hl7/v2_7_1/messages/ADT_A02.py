"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ADT_A02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.DB1 import DB1
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PDA import PDA
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_ARV = ARV
_DB1 = DB1
_EVN = EVN
_MSH = MSH
_OBX = OBX
_PD1 = PD1
_PDA = PDA
_PID = PID
_PV1 = PV1
_PV2 = PV2
_ROL = ROL
_SFT = SFT
_UAC = UAC


class ADT_A02(BaseModel):
    """HL7 v2 ADT_A02 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        ARV (Optional[List[ARV]]): optional
        ROL (Optional[List[ROL]]): optional
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        DB1 (Optional[List[DB1]]): optional
        OBX (Optional[List[OBX]]): optional
        PDA (Optional[PDA]): optional
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

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
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

    PDA: _PDA | None = Field(
        default=None,
        title="PDA",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
