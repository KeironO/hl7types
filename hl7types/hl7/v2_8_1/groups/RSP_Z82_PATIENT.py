"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_Z82.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from .RSP_Z82_VISIT import RSP_Z82_VISIT

_NTE = NTE
_PD1 = PD1
_PID = PID
_RSP_Z82_VISIT = RSP_Z82_VISIT


class RSP_Z82_PATIENT(BaseModel):
    """HL7 v2 RSP_Z82.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NTE (Optional[List[NTE]]): optional
        VISIT (Optional[RSP_Z82_VISIT]): optional
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

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VISIT: _RSP_Z82_VISIT | None = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
