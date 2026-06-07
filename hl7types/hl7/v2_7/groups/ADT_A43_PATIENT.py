"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ADT_A43.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MRG import MRG
from ..segments.PD1 import PD1
from ..segments.PID import PID

_MRG = MRG
_PD1 = PD1
_PID = PID


class ADT_A43_PATIENT(HL7Model):
    """HL7 v2 ADT_A43.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        MRG (MRG): required
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

    MRG: _MRG = Field(
        title="MRG",
        description="Required",
    )

    model_config = {"populate_by_name": True}
