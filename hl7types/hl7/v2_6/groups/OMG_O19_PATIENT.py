"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OMG_O19.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.GT1 import GT1
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .OMG_O19_INSURANCE import OMG_O19_INSURANCE
from .OMG_O19_PATIENT_VISIT import OMG_O19_PATIENT_VISIT

_AL1 = AL1
_GT1 = GT1
_NK1 = NK1
_NTE = NTE
_OMG_O19_INSURANCE = OMG_O19_INSURANCE
_OMG_O19_PATIENT_VISIT = OMG_O19_PATIENT_VISIT
_PD1 = PD1
_PID = PID


class OMG_O19_PATIENT(HL7Model):
    """HL7 v2 OMG_O19.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        PATIENT_VISIT (Optional[OMG_O19_PATIENT_VISIT]): optional
        INSURANCE (Optional[List[OMG_O19_INSURANCE]]): optional
        GT1 (Optional[GT1]): Guarantor, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Additional Demographic",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    PATIENT_VISIT: Optional[_OMG_O19_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    INSURANCE: Optional[List[_OMG_O19_INSURANCE]] = Field(
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
        description="Patient Allergy Information",
    )

    model_config = ConfigDict(populate_by_name=True)
