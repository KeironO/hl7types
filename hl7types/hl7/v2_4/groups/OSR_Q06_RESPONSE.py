"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OSR_Q06.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .OSR_Q06_ORDER import OSR_Q06_ORDER
from .OSR_Q06_PATIENT import OSR_Q06_PATIENT

_OSR_Q06_ORDER = OSR_Q06_ORDER
_OSR_Q06_PATIENT = OSR_Q06_PATIENT


class OSR_Q06_RESPONSE(BaseModel):
    """HL7 v2 OSR_Q06.RESPONSE group.

    Attributes:
        PATIENT (Optional[OSR_Q06_PATIENT]): optional
        ORDER (List[OSR_Q06_ORDER]): required
    """

    PATIENT: _OSR_Q06_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_OSR_Q06_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
