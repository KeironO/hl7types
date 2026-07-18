"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E20.PAT_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.OBX import OBX
from ..segments.PID import PID

from .EHC_E20_DIAGNOSIS import EHC_E20_DIAGNOSIS
from .EHC_E20_INSURANCE import EHC_E20_INSURANCE

_ACC = ACC
_EHC_E20_DIAGNOSIS = EHC_E20_DIAGNOSIS
_EHC_E20_INSURANCE = EHC_E20_INSURANCE
_OBX = OBX
_PID = PID


class EHC_E20_PAT_INFO(HL7Model):
    """HL7 v2 EHC_E20.PAT_INFO group.

    Attributes:
        PID (PID): Patient Identification, required
        ACC (Optional[List[ACC]]): Accident, optional
        INSURANCE (List[EHC_E20_INSURANCE]): required
        DIAGNOSIS (Optional[List[EHC_E20_DIAGNOSIS]]): optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    ACC: Optional[List[_ACC]] = Field(
        default=None,
        title="ACC",
        description="Accident",
    )

    INSURANCE: List[_EHC_E20_INSURANCE] = Field(
        min_length=1,
        title="INSURANCE",
    )

    DIAGNOSIS: Optional[List[_EHC_E20_DIAGNOSIS]] = Field(
        default=None,
        title="DIAGNOSIS",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = ConfigDict(populate_by_name=True)
