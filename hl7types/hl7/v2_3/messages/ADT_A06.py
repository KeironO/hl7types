"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A06
Type: Message
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
from ..segments.EVN import EVN
from ..segments.GT1 import GT1
from ..segments.MRG import MRG
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.UB1 import UB1
from ..segments.UB2 import UB2

from ..groups.ADT_A06_INSURANCE import ADT_A06_INSURANCE
from ..groups.ADT_A06_PROCEDURE import ADT_A06_PROCEDURE

_ACC = ACC
_ADT_A06_INSURANCE = ADT_A06_INSURANCE
_ADT_A06_PROCEDURE = ADT_A06_PROCEDURE
_AL1 = AL1
_DB1 = DB1
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_GT1 = GT1
_MRG = MRG
_MSH = MSH
_NK1 = NK1
_OBX = OBX
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2
_UB1 = UB1
_UB2 = UB2


class ADT_A06(HL7Model):
    """ADT/ACK -  Transfer an outpatient to inpatient.

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        MRG (Optional[MRG]): Merge patient information, optional
        NK1 (Optional[List[NK1]]): Next of kin, optional
        PV1 (PV1): Patient visit, required
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        DB1 (Optional[List[DB1]]): Disability Segment, optional
        DRG (Optional[DRG]): Diagnosis Related Group, optional
        OBX (Optional[List[OBX]]): Observation segment, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        PROCEDURE (Optional[List[ADT_A06_PROCEDURE]]): optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[ADT_A06_INSURANCE]]): optional
        ACC (Optional[ACC]): Accident, optional
        UB1 (Optional[UB1]): UB82  data, optional
        UB2 (Optional[UB2]): UB92 data, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    EVN: _EVN = Field(
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

    MRG: Optional[_MRG] = Field(
        default=None,
        title="MRG",
        description="Merge patient information",
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

    DRG: Optional[_DRG] = Field(
        default=None,
        title="DRG",
        description="Diagnosis Related Group",
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

    PROCEDURE: Optional[List[_ADT_A06_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    INSURANCE: Optional[List[_ADT_A06_INSURANCE]] = Field(
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

    model_config = {"populate_by_name": True}
