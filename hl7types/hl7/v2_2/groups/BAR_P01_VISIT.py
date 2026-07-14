"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: BAR_P01.VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.DG1 import DG1
from ..segments.GT1 import GT1
from ..segments.NK1 import NK1
from ..segments.OBX import OBX
from ..segments.PR1 import PR1
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.UB1 import UB1
from ..segments.UB2 import UB2

from .BAR_P01_INSURANCE import BAR_P01_INSURANCE

_ACC = ACC
_AL1 = AL1
_BAR_P01_INSURANCE = BAR_P01_INSURANCE
_DG1 = DG1
_GT1 = GT1
_NK1 = NK1
_OBX = OBX
_PR1 = PR1
_PV1 = PV1
_PV2 = PV2
_UB1 = UB1
_UB2 = UB2


class BAR_P01_VISIT(HL7Model):
    """HL7 v2 BAR_P01.VISIT group.

    Attributes:
        PV1 (Optional[PV1]): PATIENT VISIT, optional
        PV2 (Optional[PV2]): PATIENT VISIT - additional information, optional
        OBX (Optional[List[OBX]]): OBSERVATION RESULT, optional
        AL1 (Optional[List[AL1]]): PATIENT ALLERGY INFORMATION, optional
        DG1 (Optional[List[DG1]]): DIAGNOSIS, optional
        PR1 (Optional[List[PR1]]): PROCEDURES, optional
        GT1 (Optional[List[GT1]]): GUARANTOR, optional
        NK1 (Optional[List[NK1]]): NEXT OF KIN, optional
        INSURANCE (Optional[List[BAR_P01_INSURANCE]]): optional
        ACC (Optional[ACC]): ACCIDENT, optional
        UB1 (Optional[UB1]): UB82 DATA, optional
        UB2 (Optional[UB2]): UB92 DATA, optional
    """

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="PATIENT VISIT",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="PATIENT VISIT - additional information",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="OBSERVATION RESULT",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="PATIENT ALLERGY INFORMATION",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="DIAGNOSIS",
    )

    PR1: Optional[List[_PR1]] = Field(
        default=None,
        title="PR1",
        description="PROCEDURES",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="GUARANTOR",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="NEXT OF KIN",
    )

    INSURANCE: Optional[List[_BAR_P01_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="ACCIDENT",
    )

    UB1: Optional[_UB1] = Field(
        default=None,
        title="UB1",
        description="UB82 DATA",
    )

    UB2: Optional[_UB2] = Field(
        default=None,
        title="UB2",
        description="UB92 DATA",
    )

    model_config = {"populate_by_name": True}
