"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORN_O02.RESPONSE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .ORN_O02_ORDER import ORN_O02_ORDER
from .ORN_O02_PATIENT import ORN_O02_PATIENT

_ORN_O02_ORDER = ORN_O02_ORDER
_ORN_O02_PATIENT = ORN_O02_PATIENT


class ORN_O02_RESPONSE(BaseModel):
    """HL7 v2 ORN_O02.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORN_O02_PATIENT]): optional
        ORDER (List[ORN_O02_ORDER]): required
    """

    PATIENT: Optional[_ORN_O02_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_ORN_O02_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
