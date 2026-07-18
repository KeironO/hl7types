"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_Z82.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .RSP_Z82_VISIT import RSP_Z82_VISIT

_NTE = NTE
_PD1 = PD1
_PID = PID
_RSP_Z82_VISIT = RSP_Z82_VISIT


class RSP_Z82_PATIENT(HL7Model):
    """HL7 v2 RSP_Z82.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VISIT (Optional[RSP_Z82_VISIT]): optional
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

    VISIT: Optional[_RSP_Z82_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    model_config = ConfigDict(populate_by_name=True)
