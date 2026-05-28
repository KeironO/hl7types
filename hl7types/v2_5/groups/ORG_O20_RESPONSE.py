"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORG_O20.RESPONSE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .ORG_O20_ORDER import ORG_O20_ORDER
from .ORG_O20_PATIENT import ORG_O20_PATIENT

_ORG_O20_ORDER = ORG_O20_ORDER
_ORG_O20_PATIENT = ORG_O20_PATIENT


class ORG_O20_RESPONSE(BaseModel):
    """HL7 v2 ORG_O20.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORG_O20_PATIENT]): optional
        ORDER (List[ORG_O20_ORDER]): required
    """

    PATIENT: Optional[_ORG_O20_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_ORG_O20_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
