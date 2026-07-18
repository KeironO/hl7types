"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ARD_A19.QUERY_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.DB1 import DB1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.EVN import EVN
from ..segments.GT1 import GT1
from ..segments.NK1 import NK1
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.UB1 import UB1
from ..segments.UB2 import UB2

from .ARD_A19_INSURANCE import ARD_A19_INSURANCE
from .ARD_A19_PROCEDURE import ARD_A19_PROCEDURE

_ACC = ACC
_AL1 = AL1
_ARD_A19_INSURANCE = ARD_A19_INSURANCE
_ARD_A19_PROCEDURE = ARD_A19_PROCEDURE
_DB1 = DB1
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_GT1 = GT1
_NK1 = NK1
_OBX = OBX
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2
_UB1 = UB1
_UB2 = UB2


class ARD_A19_QUERY_RESPONSE(HL7Model):
    """HL7 v2 ARD_A19.QUERY_RESPONSE group.

    Attributes:
        EVN (Optional[EVN]): Event type, optional
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        NK1 (Optional[List[NK1]]): Next of kin, optional
        PV1 (PV1): Patient visit, required
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        DB1 (Optional[List[DB1]]): Disability Segment, optional
        OBX (Optional[List[OBX]]): Observation segment, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[DRG]): Diagnosis Related Group, optional
        PROCEDURE (Optional[List[ARD_A19_PROCEDURE]]): optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[ARD_A19_INSURANCE]]): optional
        ACC (Optional[ACC]): Accident, optional
        UB1 (Optional[UB1]): UB82  data, optional
        UB2 (Optional[UB2]): UB92 data, optional
    """

    EVN: Optional[_EVN] = Field(
        default=None,
        title="EVN",
        description="Event type",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Demographic",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of kin",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient visit - additional information",
    )

    DB1: Optional[List[_DB1]] = Field(
        default=None,
        title="DB1",
        description="Disability Segment",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation segment",
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

    PROCEDURE: Optional[List[_ARD_A19_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    INSURANCE: Optional[List[_ARD_A19_INSURANCE]] = Field(
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
        description="UB82  data",
    )

    UB2: Optional[_UB2] = Field(
        default=None,
        title="UB2",
        description="UB92 data",
    )

    model_config = ConfigDict(populate_by_name=True)
