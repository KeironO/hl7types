"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMG_O19.PATIENT_PRIOR
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

_ARV = ARV
_PD1 = PD1
_PID = PID
_PRT = PRT


class OMG_O19_PATIENT_PRIOR(BaseModel):
    """HL7 v2 OMG_O19.PATIENT_PRIOR group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        ARV (Optional[List[ARV]]): optional
        PRT (Optional[List[PRT]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: _PD1 | None = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
