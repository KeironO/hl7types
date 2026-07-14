"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: BAR_P01.VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.DB1 import DB1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.GT1 import GT1
from ..segments.NK1 import NK1
from ..segments.OBX import OBX
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.UB1 import UB1
from ..segments.UB2 import UB2

from .BAR_P01_INSURANCE import BAR_P01_INSURANCE
from .BAR_P01_PROCEDURE import BAR_P01_PROCEDURE

_ACC = ACC
_AL1 = AL1
_BAR_P01_INSURANCE = BAR_P01_INSURANCE
_BAR_P01_PROCEDURE = BAR_P01_PROCEDURE
_DB1 = DB1
_DG1 = DG1
_DRG = DRG
_GT1 = GT1
_NK1 = NK1
_OBX = OBX
_PV1 = PV1
_PV2 = PV2
_UB1 = UB1
_UB2 = UB2


class BAR_P01_VISIT(HL7Model):
    """HL7 v2 BAR_P01.VISIT group.

    Attributes:
        PV1 (Optional[PV1]): PV1 - patient visit segment-, optional
        PV2 (Optional[PV2]): PV2 - patient visit - additional information segment, optional
        DB1 (Optional[List[DB1]]): DB1 - Disability segment, optional
        OBX (Optional[List[OBX]]): OBX - observation/result segment, optional
        AL1 (Optional[List[AL1]]): AL1 - patient allergy information segment, optional
        DG1 (Optional[List[DG1]]): DG1 - diagnosis segment, optional
        DRG (Optional[DRG]): DRG - diagnosis related group segment, optional
        PROCEDURE (Optional[List[BAR_P01_PROCEDURE]]): optional
        GT1 (Optional[List[GT1]]): GT1 - guarantor segment, optional
        NK1 (Optional[List[NK1]]): NK1 - next of kin / associated parties segment-, optional
        INSURANCE (Optional[List[BAR_P01_INSURANCE]]): optional
        ACC (Optional[ACC]): ACC - accident segment, optional
        UB1 (Optional[UB1]): UB1 - UB82 data segment, optional
        UB2 (Optional[UB2]): UB2 - UB92 data segment, optional
    """

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="PV1 - patient visit segment-",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="PV2 - patient visit - additional information segment",
    )

    DB1: Optional[List[_DB1]] = Field(
        default=None,
        title="DB1",
        description="DB1 - Disability segment",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="OBX - observation/result segment",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="AL1 - patient allergy information segment",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="DG1 - diagnosis segment",
    )

    DRG: Optional[_DRG] = Field(
        default=None,
        title="DRG",
        description="DRG - diagnosis related group segment",
    )

    PROCEDURE: Optional[List[_BAR_P01_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="GT1 - guarantor segment",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="NK1 - next of kin / associated parties segment-",
    )

    INSURANCE: Optional[List[_BAR_P01_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="ACC - accident segment",
    )

    UB1: Optional[_UB1] = Field(
        default=None,
        title="UB1",
        description="UB1 - UB82 data segment",
    )

    UB2: Optional[_UB2] = Field(
        default=None,
        title="UB2",
        description="UB2 - UB92 data segment",
    )

    model_config = {"populate_by_name": True}
