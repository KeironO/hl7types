"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RDS_O13.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.NTE import NTE
from ..segments.PID import PID

from .RDS_O13_ADDITIONAL_DEMOGRAPHICS import RDS_O13_ADDITIONAL_DEMOGRAPHICS
from .RDS_O13_PATIENT_VISIT import RDS_O13_PATIENT_VISIT

_AL1 = AL1
_NTE = NTE
_PID = PID
_RDS_O13_ADDITIONAL_DEMOGRAPHICS = RDS_O13_ADDITIONAL_DEMOGRAPHICS
_RDS_O13_PATIENT_VISIT = RDS_O13_PATIENT_VISIT


class RDS_O13_PATIENT(HL7Model):
    """HL7 v2 RDS_O13.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        ADDITIONAL_DEMOGRAPHICS (Optional[RDS_O13_ADDITIONAL_DEMOGRAPHICS]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
        PATIENT_VISIT (Optional[RDS_O13_PATIENT_VISIT]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    ADDITIONAL_DEMOGRAPHICS: Optional[_RDS_O13_ADDITIONAL_DEMOGRAPHICS] = Field(
        default=None,
        title="ADDITIONAL_DEMOGRAPHICS",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient Allergy Information",
    )

    PATIENT_VISIT: Optional[_RDS_O13_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    model_config = ConfigDict(populate_by_name=True)
