"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORP_O10.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .ORP_O10_ORDER import ORP_O10_ORDER
from .ORP_O10_PATIENT import ORP_O10_PATIENT

_ORP_O10_ORDER = ORP_O10_ORDER
_ORP_O10_PATIENT = ORP_O10_PATIENT


class ORP_O10_RESPONSE(BaseModel):
    """HL7 v2 ORP_O10.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORP_O10_PATIENT]): optional
        ORDER (List[ORP_O10_ORDER]): required
    """

    PATIENT: _ORP_O10_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_ORP_O10_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
