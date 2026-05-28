"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRO_O02.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .RRO_O02_ORDER import RRO_O02_ORDER
from .RRO_O02_PATIENT import RRO_O02_PATIENT

_RRO_O02_ORDER = RRO_O02_ORDER
_RRO_O02_PATIENT = RRO_O02_PATIENT


class RRO_O02_RESPONSE(BaseModel):
    """HL7 v2 RRO_O02.RESPONSE group.

    Attributes:
        PATIENT (Optional[RRO_O02_PATIENT]): optional
        ORDER (List[RRO_O02_ORDER]): required
    """

    PATIENT: _RRO_O02_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RRO_O02_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
