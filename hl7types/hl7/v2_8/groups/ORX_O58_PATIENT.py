"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORX_O58.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.PRT import PRT

_ARV = ARV
_NTE = NTE
_PID = PID
_PRT = PRT


class ORX_O58_PATIENT(BaseModel):
    """HL7 v2 ORX_O58.PATIENT group.

    Attributes:
        PID (PID): required
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
