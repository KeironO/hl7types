"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R21.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID

from .OUL_R21_VISIT import OUL_R21_VISIT

_NTE = NTE
_OUL_R21_VISIT = OUL_R21_VISIT
_PD1 = PD1
_PID = PID


class OUL_R21_PATIENT(BaseModel):
    """HL7 v2 OUL_R21.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        VISIT (Optional[OUL_R21_VISIT]): optional
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

    VISIT: Optional[_OUL_R21_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
