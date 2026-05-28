"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BAR_P05.VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ABS import ABS
from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.BLC import BLC
from ..segments.DB1 import DB1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.GT1 import GT1
from ..segments.NK1 import NK1
from ..segments.OBX import OBX
from ..segments.PRT import PRT
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.RMI import RMI
from ..segments.ROL import ROL
from ..segments.UB1 import UB1
from ..segments.UB2 import UB2

from .BAR_P05_INSURANCE import BAR_P05_INSURANCE
from .BAR_P05_PROCEDURE import BAR_P05_PROCEDURE

_ABS = ABS
_ACC = ACC
_AL1 = AL1
_BAR_P05_INSURANCE = BAR_P05_INSURANCE
_BAR_P05_PROCEDURE = BAR_P05_PROCEDURE
_BLC = BLC
_DB1 = DB1
_DG1 = DG1
_DRG = DRG
_GT1 = GT1
_NK1 = NK1
_OBX = OBX
_PRT = PRT
_PV1 = PV1
_PV2 = PV2
_RMI = RMI
_ROL = ROL
_UB1 = UB1
_UB2 = UB2


class BAR_P05_VISIT(BaseModel):
    """HL7 v2 BAR_P05.VISIT group.

    Attributes:
        PV1 (Optional[PV1]): optional
        PV2 (Optional[PV2]): optional
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
        DB1 (Optional[List[DB1]]): optional
        OBX (Optional[List[OBX]]): optional
        AL1 (Optional[List[AL1]]): optional
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[DRG]): optional
        PROCEDURE (Optional[List[BAR_P05_PROCEDURE]]): optional
        GT1 (Optional[List[GT1]]): optional
        NK1 (Optional[List[NK1]]): optional
        INSURANCE (Optional[List[BAR_P05_INSURANCE]]): optional
        ACC (Optional[ACC]): optional
        UB1 (Optional[UB1]): optional
        UB2 (Optional[UB2]): optional
        ABS (Optional[ABS]): optional
        BLC (Optional[List[BLC]]): optional
        RMI (Optional[RMI]): optional
    """

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Optional",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    DB1: Optional[List[_DB1]] = Field(
        default=None,
        title="DB1",
        description="Optional, repeating",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    DRG: Optional[_DRG] = Field(
        default=None,
        title="DRG",
        description="Optional",
    )

    PROCEDURE: Optional[List[_BAR_P05_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
        description="Optional, repeating",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    INSURANCE: Optional[List[_BAR_P05_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="Optional",
    )

    UB1: Optional[_UB1] = Field(
        default=None,
        title="UB1",
        description="Optional",
    )

    UB2: Optional[_UB2] = Field(
        default=None,
        title="UB2",
        description="Optional",
    )

    ABS: Optional[_ABS] = Field(
        default=None,
        title="ABS",
        description="Optional",
    )

    BLC: Optional[List[_BLC]] = Field(
        default=None,
        title="BLC",
        description="Optional, repeating",
    )

    RMI: Optional[_RMI] = Field(
        default=None,
        title="RMI",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
