"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_Z88.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .RSP_Z88_ALLERGY import RSP_Z88_ALLERGY

_NTE = NTE
_PD1 = PD1
_PID = PID
_RSP_Z88_ALLERGY = RSP_Z88_ALLERGY


class RSP_Z88_PATIENT(BaseModel):
    """HL7 v2 RSP_Z88.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        ALLERGY (Optional[RSP_Z88_ALLERGY]): optional
    """

    PID: _PID = Field(
        default=...,
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

    ALLERGY: Optional[_RSP_Z88_ALLERGY] = Field(
        default=None,
        title="ALLERGY",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
