"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRA_O02.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .RRA_O02_ORDER import RRA_O02_ORDER
from .RRA_O02_PATIENT import RRA_O02_PATIENT

_RRA_O02_ORDER = RRA_O02_ORDER
_RRA_O02_PATIENT = RRA_O02_PATIENT


class RRA_O02_RESPONSE(BaseModel):
    """HL7 v2 RRA_O02.RESPONSE group.

    Attributes:
        PATIENT (Optional[RRA_O02_PATIENT]): optional
        ORDER (List[RRA_O02_ORDER]): required
    """

    PATIENT: _RRA_O02_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RRA_O02_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
