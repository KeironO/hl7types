"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RRG_O16.RESPONSE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
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

    PATIENT: Optional[_RRG_O16_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RRG_O16_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
