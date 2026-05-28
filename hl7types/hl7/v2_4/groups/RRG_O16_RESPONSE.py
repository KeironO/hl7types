"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RRG_O16.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .RRG_O16_ORDER import RRG_O16_ORDER
from .RRG_O16_PATIENT import RRG_O16_PATIENT

_RRG_O16_ORDER = RRG_O16_ORDER
_RRG_O16_PATIENT = RRG_O16_PATIENT


class RRG_O16_RESPONSE(BaseModel):
    """HL7 v2 RRG_O16.RESPONSE group.

    Attributes:
        PATIENT (Optional[RRG_O16_PATIENT]): optional
        ORDER (List[RRG_O16_ORDER]): required
    """

    PATIENT: _RRG_O16_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RRG_O16_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
