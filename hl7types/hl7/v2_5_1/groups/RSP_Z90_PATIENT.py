"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RSP_Z90.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .RSP_Z90_VISIT import RSP_Z90_VISIT

_NK1 = NK1
_NTE = NTE
_PD1 = PD1
_PID = PID
_RSP_Z90_VISIT = RSP_Z90_VISIT


class RSP_Z90_PATIENT(HL7Model):
    """HL7 v2 RSP_Z90.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VISIT (Optional[RSP_Z90_VISIT]): optional
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

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    VISIT: Optional[_RSP_Z90_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    model_config = {"populate_by_name": True}
