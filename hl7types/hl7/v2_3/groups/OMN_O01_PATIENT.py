"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OMN_O01.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.GT1 import GT1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .OMN_O01_INSURANCE import OMN_O01_INSURANCE
from .OMN_O01_PATIENT_VISIT import OMN_O01_PATIENT_VISIT

_AL1 = AL1
_GT1 = GT1
_NTE = NTE
_OMN_O01_INSURANCE = OMN_O01_INSURANCE
_OMN_O01_PATIENT_VISIT = OMN_O01_PATIENT_VISIT
_PD1 = PD1
_PID = PID


class OMN_O01_PATIENT(HL7Model):
    """HL7 v2 OMN_O01.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        PATIENT_VISIT (Optional[OMN_O01_PATIENT_VISIT]): optional
        INSURANCE (Optional[List[OMN_O01_INSURANCE]]): optional
        GT1 (Optional[GT1]): Guarantor, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Demographic",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    PATIENT_VISIT: Optional[_OMN_O01_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    INSURANCE: Optional[List[_OMN_O01_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    GT1: Optional[_GT1] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient allergy information",
    )

    model_config = ConfigDict(populate_by_name=True)
