"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDS_O01.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .RDS_O01_PATIENT_VISIT import RDS_O01_PATIENT_VISIT

_AL1 = AL1
_NTE = NTE
_PD1 = PD1
_PID = PID
_RDS_O01_PATIENT_VISIT = RDS_O01_PATIENT_VISIT


class RDS_O01_PATIENT(HL7Model):
    """HL7 v2 RDS_O01.PATIENT group.

    Attributes:
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        AL1 (Optional[List[AL1]]): AL1 - patient allergy information segment, optional
        PATIENT_VISIT (Optional[RDS_O01_PATIENT_VISIT]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="PD1 - patient additional demographic segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="AL1 - patient allergy information segment",
    )

    PATIENT_VISIT: Optional[_RDS_O01_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    model_config = ConfigDict(populate_by_name=True)
