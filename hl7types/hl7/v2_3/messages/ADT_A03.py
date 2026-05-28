"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A03
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ADT_A03_PROCEDURE import ADT_A03_PROCEDURE
from ..segments.DB1 import DB1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_ADT_A03_PROCEDURE = ADT_A03_PROCEDURE
_DB1 = DB1
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_MSH = MSH
_OBX = OBX
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2


class ADT_A03(BaseModel):
    """HL7 v2 ADT_A03 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PV1 (PV1): required
        PV2 (Optional[PV2]): optional
        DB1 (Optional[List[DB1]]): optional
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[DRG]): optional
        PROCEDURE (Optional[List[ADT_A03_PROCEDURE]]): optional
        OBX (Optional[List[OBX]]): optional
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

    PROCEDURE: list[_ADT_A03_PROCEDURE] | None = Field(
        default=None,
        title="PROCEDURE",
        description="Optional, repeating",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
