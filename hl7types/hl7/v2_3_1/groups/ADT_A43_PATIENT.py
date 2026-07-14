"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        MRG (MRG): MRG - merge patient information segment-, required
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

    MRG: _MRG = Field(
        title="MRG",
        description="MRG - merge patient information segment-",
    )

    model_config = {"populate_by_name": True}
