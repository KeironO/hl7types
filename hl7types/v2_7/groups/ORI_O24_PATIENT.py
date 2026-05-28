"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORI_O24.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.PRT import PRT

_NTE = NTE
_PID = PID
_PRT = PRT


class ORI_O24_PATIENT(BaseModel):
    """HL7 v2 ORI_O24.PATIENT group.

    Attributes:
        PID (PID): required
        NTE (Optional[List[NTE]]): optional
        PRT (Optional[List[PRT]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
