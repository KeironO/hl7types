"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OML_O33.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.GT1 import GT1
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .OML_O33_INSURANCE import OML_O33_INSURANCE
from .OML_O33_PATIENT_VISIT import OML_O33_PATIENT_VISIT

_AL1 = AL1
_GT1 = GT1
_NK1 = NK1
_NTE = NTE
_OML_O33_INSURANCE = OML_O33_INSURANCE
_OML_O33_PATIENT_VISIT = OML_O33_PATIENT_VISIT
_PD1 = PD1
_PID = PID


class OML_O33_PATIENT(HL7Model):
    """HL7 v2 OML_O33.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        NK1 (Optional[List[NK1]]): optional
        PATIENT_VISIT (Optional[OML_O33_PATIENT_VISIT]): optional
        INSURANCE (Optional[List[OML_O33_INSURANCE]]): optional
        GT1 (Optional[GT1]): optional
        AL1 (Optional[List[AL1]]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    PATIENT_VISIT: Optional[_OML_O33_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    INSURANCE: Optional[List[_OML_O33_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    GT1: Optional[_GT1] = Field(
        default=None,
        title="GT1",
        description="Optional",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
