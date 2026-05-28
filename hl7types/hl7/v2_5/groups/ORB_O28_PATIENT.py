"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORB_O28.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PID import PID
from .ORB_O28_ORDER import ORB_O28_ORDER

_ORB_O28_ORDER = ORB_O28_ORDER
_PID = PID


class ORB_O28_PATIENT(BaseModel):
    """HL7 v2 ORB_O28.PATIENT group.

    Attributes:
        PID (PID): required
        ORDER (Optional[List[ORB_O28_ORDER]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    ORDER: list[_ORB_O28_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
