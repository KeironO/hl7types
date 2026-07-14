"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E01.PATIENT_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

from .EHC_E01_DIAGNOSIS import EHC_E01_DIAGNOSIS
from .EHC_E01_INSURANCE import EHC_E01_INSURANCE

_ACC = ACC
_EHC_E01_DIAGNOSIS = EHC_E01_DIAGNOSIS
_EHC_E01_INSURANCE = EHC_E01_INSURANCE
_OBX = OBX
_PID = PID
_PV1 = PV1
_PV2 = PV2


class EHC_E01_PATIENT_INFO(HL7Model):
    """HL7 v2 EHC_E01.PATIENT_INFO group.

    Attributes:
        PID (PID): Patient Identification, required
        PV1 (Optional[PV1]): Patient Visit, optional
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
        ACC (Optional[List[ACC]]): Accident, optional
        INSURANCE (List[EHC_E01_INSURANCE]): required
        DIAGNOSIS (Optional[List[EHC_E01_DIAGNOSIS]]): optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Patient Visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient Visit - Additional Information",
    )

    ACC: Optional[List[_ACC]] = Field(
        default=None,
        title="ACC",
        description="Accident",
    )

    INSURANCE: List[_EHC_E01_INSURANCE] = Field(
        min_length=1,
        title="INSURANCE",
    )

    DIAGNOSIS: Optional[List[_EHC_E01_DIAGNOSIS]] = Field(
        default=None,
        title="DIAGNOSIS",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = {"populate_by_name": True}
