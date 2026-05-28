"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORN_O08.RESPONSE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .ORN_O08_ORDER import ORN_O08_ORDER
from .ORN_O08_PATIENT import ORN_O08_PATIENT

_ORN_O08_ORDER = ORN_O08_ORDER
_ORN_O08_PATIENT = ORN_O08_PATIENT


class ORN_O08_RESPONSE(BaseModel):
    """HL7 v2 ORN_O08.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORN_O08_PATIENT]): optional
        ORDER (List[ORN_O08_ORDER]): required
    """

    PATIENT: Optional[_ORN_O08_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_ORN_O08_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
