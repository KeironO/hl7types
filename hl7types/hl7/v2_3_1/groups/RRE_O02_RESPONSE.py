"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRE_O02.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .RRE_O02_ORDER import RRE_O02_ORDER
from .RRE_O02_PATIENT import RRE_O02_PATIENT

_RRE_O02_ORDER = RRE_O02_ORDER
_RRE_O02_PATIENT = RRE_O02_PATIENT


class RRE_O02_RESPONSE(BaseModel):
    """HL7 v2 RRE_O02.RESPONSE group.

    Attributes:
        PATIENT (Optional[RRE_O02_PATIENT]): optional
        ORDER (List[RRE_O02_ORDER]): required
    """

    PATIENT: Optional[_RRE_O02_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RRE_O02_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
