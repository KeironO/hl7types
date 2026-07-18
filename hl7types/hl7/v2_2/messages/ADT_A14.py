"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ADT_A14
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.DG1 import DG1
from ..segments.EVN import EVN
from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PR1 import PR1
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.UB1 import UB1
from ..segments.UB2 import UB2

from ..groups.ADT_A14_INSURANCE import ADT_A14_INSURANCE

_ACC = ACC
_ADT_A14_INSURANCE = ADT_A14_INSURANCE
_AL1 = AL1
_DG1 = DG1
_EVN = EVN
_GT1 = GT1
_MSH = MSH
_NK1 = NK1
_OBX = OBX
_PID = PID
_PR1 = PR1
_PV1 = PV1
_PV2 = PV2
_UB1 = UB1
_UB2 = UB2


class ADT_A14(HL7Model):
    """HL7 v2 ADT_A14 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        EVN (EVN): EVENT TYPE, required
        PID (PID): PATIENT IDENTIFICATION, required
        NK1 (Optional[List[NK1]]): NEXT OF KIN, optional
        PV1 (PV1): PATIENT VISIT, required
        PV2 (Optional[PV2]): PATIENT VISIT - additional information, optional
        OBX (Optional[List[OBX]]): OBSERVATION RESULT, optional
        AL1 (Optional[List[AL1]]): PATIENT ALLERGY INFORMATION, optional
        DG1 (Optional[List[DG1]]): DIAGNOSIS, optional
        PR1 (Optional[List[PR1]]): PROCEDURES, optional
        GT1 (Optional[List[GT1]]): GUARANTOR, optional
        INSURANCE (Optional[List[ADT_A14_INSURANCE]]): optional
        ACC (Optional[ACC]): ACCIDENT, optional
        UB1 (Optional[UB1]): UB82 DATA, optional
        UB2 (Optional[UB2]): UB92 DATA, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="EVENT TYPE",
    )

    PID: _PID = Field(
        title="PID",
        description="PATIENT IDENTIFICATION",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="NEXT OF KIN",
    )

    PV1: _PV1 = Field(
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

    INSURANCE: Optional[List[_ADT_A14_INSURANCE]] = Field(
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

    model_config = ConfigDict(populate_by_name=True)
