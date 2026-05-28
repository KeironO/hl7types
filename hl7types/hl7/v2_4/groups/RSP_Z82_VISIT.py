"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z82.VISIT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from .RSP_Z82_PATIENT_VISIT import RSP_Z82_PATIENT_VISIT

_AL1 = AL1
_RSP_Z82_PATIENT_VISIT = RSP_Z82_PATIENT_VISIT


class RSP_Z82_VISIT(BaseModel):
    """HL7 v2 RSP_Z82.VISIT group.

    Attributes:
        AL1 (List[AL1]): required
        PATIENT_VISIT (Optional[RSP_Z82_PATIENT_VISIT]): optional
    """

    AL1: list[_AL1] = Field(
        default=...,
        title="AL1",
        description="Required, repeating",
    )

    PATIENT_VISIT: _RSP_Z82_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
