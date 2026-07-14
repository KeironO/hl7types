"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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
from ..segments.ROL import ROL
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
_ROL = ROL
_UB1 = UB1
_UB2 = UB2


class BAR_P01_VISIT(HL7Model):
    """HL7 v2 BAR_P01.VISIT group.

    Attributes:
        PV1 (Optional[PV1]): Patient visit, optional
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        ROL (Optional[List[ROL]]): Role, optional
        DB1 (Optional[List[DB1]]): Disability, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[DRG]): Diagnosis Related Group, optional
        PROCEDURE (Optional[List[BAR_P01_PROCEDURE]]): optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        NK1 (Optional[List[NK1]]): Next of kin / associated parties, optional
        INSURANCE (Optional[List[BAR_P01_INSURANCE]]): optional
        ACC (Optional[ACC]): Accident, optional
        UB1 (Optional[UB1]): UB82, optional
        UB2 (Optional[UB2]): UB92 Data, optional
    """

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Patient visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient visit - additional information",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    DB1: Optional[List[_DB1]] = Field(
        default=None,
        title="DB1",
        description="Disability",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient allergy information",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    DRG: Optional[_DRG] = Field(
        default=None,
        title="DRG",
        description="Diagnosis Related Group",
    )

    PROCEDURE: Optional[List[_BAR_P01_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of kin / associated parties",
    )

    INSURANCE: Optional[List[_BAR_P01_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="Accident",
    )

    UB1: Optional[_UB1] = Field(
        default=None,
        title="UB1",
        description="UB82",
    )

    UB2: Optional[_UB2] = Field(
        default=None,
        title="UB2",
        description="UB92 Data",
    )

    model_config = {"populate_by_name": True}
