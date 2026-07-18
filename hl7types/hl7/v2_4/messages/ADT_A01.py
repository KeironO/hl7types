"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A01
Type: Message
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
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PDA import PDA
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.ROL import ROL
from ..segments.UB1 import UB1
from ..segments.UB2 import UB2

from ..groups.ADT_A01_INSURANCE import ADT_A01_INSURANCE
from ..groups.ADT_A01_PROCEDURE import ADT_A01_PROCEDURE

_ACC = ACC
_ADT_A01_INSURANCE = ADT_A01_INSURANCE
_ADT_A01_PROCEDURE = ADT_A01_PROCEDURE
_AL1 = AL1
_DB1 = DB1
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_GT1 = GT1
_MSH = MSH
_NK1 = NK1
_OBX = OBX
_PD1 = PD1
_PDA = PDA
_PID = PID
_PV1 = PV1
_PV2 = PV2
_ROL = ROL
_UB1 = UB1
_UB2 = UB2


class ADT_A01(HL7Model):
    """ADT/ACK - Admit / visit notification (S3).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        ROL (Optional[List[ROL]]): Role, optional
        NK1 (Optional[List[NK1]]): Next of kin / associated parties, optional
        PV1 (PV1): Patient visit, required
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        DB1 (Optional[List[DB1]]): Disability, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[DRG]): Diagnosis Related Group, optional
        PROCEDURE (Optional[List[ADT_A01_PROCEDURE]]): optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[ADT_A01_INSURANCE]]): optional
        ACC (Optional[ACC]): Accident, optional
        UB1 (Optional[UB1]): UB82, optional
        UB2 (Optional[UB2]): UB92 Data, optional
        PDA (Optional[PDA]): Patient death and autopsy, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="patient additional demographic",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of kin / associated parties",
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

    PROCEDURE: Optional[List[_ADT_A01_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    INSURANCE: Optional[List[_ADT_A01_INSURANCE]] = Field(
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

    PDA: Optional[_PDA] = Field(
        default=None,
        title="PDA",
        description="Patient death and autopsy",
    )

    model_config = ConfigDict(populate_by_name=True)
