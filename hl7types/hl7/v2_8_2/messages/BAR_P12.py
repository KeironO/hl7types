"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: BAR_P12
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.BAR_P12_PROCEDURE import BAR_P12_PROCEDURE
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_BAR_P12_PROCEDURE = BAR_P12_PROCEDURE
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_MSH = MSH
_OBX = OBX
_PID = PID
_PV1 = PV1
_SFT = SFT
_UAC = UAC


class BAR_P12(BaseModel):
    """HL7 v2 BAR_P12 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        PV1 (PV1): required
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[DRG]): optional
        PROCEDURE (Optional[List[BAR_P12_PROCEDURE]]): optional
        OBX (Optional[OBX]): optional
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

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    DG1: list[_DG1] | None = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    DRG: _DRG | None = Field(
        default=None,
        title="DRG",
        description="Optional",
    )

    PROCEDURE: list[_BAR_P12_PROCEDURE] | None = Field(
        default=None,
        title="PROCEDURE",
        description="Optional, repeating",
    )

    OBX: _OBX | None = Field(
        default=None,
        title="OBX",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
