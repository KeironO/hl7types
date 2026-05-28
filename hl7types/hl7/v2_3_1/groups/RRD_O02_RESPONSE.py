"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRD_O02.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .RRD_O02_ORDER import RRD_O02_ORDER
from .RRD_O02_PATIENT import RRD_O02_PATIENT

_RRD_O02_ORDER = RRD_O02_ORDER
_RRD_O02_PATIENT = RRD_O02_PATIENT


class RRD_O02_RESPONSE(BaseModel):
    """HL7 v2 RRD_O02.RESPONSE group.

    Attributes:
        PATIENT (Optional[RRD_O02_PATIENT]): optional
        ORDER (List[RRD_O02_ORDER]): required
    """

    PATIENT: _RRD_O02_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RRD_O02_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
