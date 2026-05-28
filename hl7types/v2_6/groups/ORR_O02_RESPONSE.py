"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORR_O02.RESPONSE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .ORR_O02_ORDER import ORR_O02_ORDER
from .ORR_O02_PATIENT import ORR_O02_PATIENT

_ORR_O02_ORDER = ORR_O02_ORDER
_ORR_O02_PATIENT = ORR_O02_PATIENT


class ORR_O02_RESPONSE(BaseModel):
    """HL7 v2 ORR_O02.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORR_O02_PATIENT]): optional
        ORDER (List[ORR_O02_ORDER]): required
    """

    PATIENT: Optional[_ORR_O02_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_ORR_O02_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
