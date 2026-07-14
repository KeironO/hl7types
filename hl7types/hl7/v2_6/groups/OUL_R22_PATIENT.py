"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R22.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .OUL_R22_VISIT import OUL_R22_VISIT

_NTE = NTE
_OBX = OBX
_OUL_R22_VISIT = OUL_R22_VISIT
_PD1 = PD1
_PID = PID


class OUL_R22_PATIENT(HL7Model):
    """HL7 v2 OUL_R22.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
        VISIT (Optional[OUL_R22_VISIT]): optional
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

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    VISIT: Optional[_OUL_R22_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    model_config = {"populate_by_name": True}
