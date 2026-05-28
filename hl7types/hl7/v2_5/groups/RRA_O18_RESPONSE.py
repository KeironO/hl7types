"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RRA_O18.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .RRA_O18_ORDER import RRA_O18_ORDER
from .RRA_O18_PATIENT import RRA_O18_PATIENT

_RRA_O18_ORDER = RRA_O18_ORDER
_RRA_O18_PATIENT = RRA_O18_PATIENT


class RRA_O18_RESPONSE(BaseModel):
    """HL7 v2 RRA_O18.RESPONSE group.

    Attributes:
        PATIENT (Optional[RRA_O18_PATIENT]): optional
        ORDER (List[RRA_O18_ORDER]): required
    """

    PATIENT: _RRA_O18_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RRA_O18_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
