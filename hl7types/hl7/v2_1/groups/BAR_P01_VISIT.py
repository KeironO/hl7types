"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: BAR_P01.VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.DG1 import DG1
from ..segments.GT1 import GT1
from ..segments.IN1 import IN1
from ..segments.NK1 import NK1
from ..segments.PR1 import PR1
from ..segments.PV1 import PV1
from ..segments.UB1 import UB1

_ACC = ACC
_DG1 = DG1
_GT1 = GT1
_IN1 = IN1
_NK1 = NK1
_PR1 = PR1
_PV1 = PV1
_UB1 = UB1


class BAR_P01_VISIT(HL7Model):
    """HL7 v2 BAR_P01.VISIT group.

    Attributes:
        PV1 (Optional[PV1]): PATIENT VISIT, optional
        DG1 (Optional[List[DG1]]): DIAGNOSIS, optional
        PR1 (Optional[List[PR1]]): PROCEDURES, optional
        GT1 (Optional[List[GT1]]): GUARANTOR, optional
        NK1 (Optional[List[NK1]]): NEXT OF KIN, optional
        IN1 (Optional[List[IN1]]): INSURANCE, optional
        ACC (Optional[ACC]): ACCIDENT, optional
        UB1 (Optional[UB1]): UB82 DATA, optional
    """

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="PATIENT VISIT",
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

    IN1: Optional[List[_IN1]] = Field(
        default=None,
        title="IN1",
        description="INSURANCE",
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

    model_config = {"populate_by_name": True}
