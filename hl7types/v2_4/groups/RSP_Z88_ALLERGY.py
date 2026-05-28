"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z88.ALLERGY
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.AL1 import AL1

from .RSP_Z88_VISIT import RSP_Z88_VISIT

_AL1 = AL1
_RSP_Z88_VISIT = RSP_Z88_VISIT


class RSP_Z88_ALLERGY(BaseModel):
    """HL7 v2 RSP_Z88.ALLERGY group.

    Attributes:
        AL1 (List[AL1]): required
        VISIT (Optional[RSP_Z88_VISIT]): optional
    """

    AL1: List[_AL1] = Field(
        default=...,
        title="AL1",
        description="Required, repeating",
    )

    VISIT: Optional[_RSP_Z88_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
