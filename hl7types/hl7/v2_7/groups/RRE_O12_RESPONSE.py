"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RRE_O12.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .RRE_O12_ORDER import RRE_O12_ORDER
from .RRE_O12_PATIENT import RRE_O12_PATIENT

_RRE_O12_ORDER = RRE_O12_ORDER
_RRE_O12_PATIENT = RRE_O12_PATIENT


class RRE_O12_RESPONSE(BaseModel):
    """HL7 v2 RRE_O12.RESPONSE group.

    Attributes:
        PATIENT (Optional[RRE_O12_PATIENT]): optional
        ORDER (List[RRE_O12_ORDER]): required
    """

    PATIENT: _RRE_O12_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RRE_O12_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
