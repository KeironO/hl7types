"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O44.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .ORL_O44_ORDER import ORL_O44_ORDER
from .ORL_O44_PATIENT import ORL_O44_PATIENT

_ORL_O44_ORDER = ORL_O44_ORDER
_ORL_O44_PATIENT = ORL_O44_PATIENT


class ORL_O44_RESPONSE(BaseModel):
    """HL7 v2 ORL_O44.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORL_O44_PATIENT]): optional
        ORDER (Optional[List[ORL_O44_ORDER]]): optional
    """

    PATIENT: _ORL_O44_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_ORL_O44_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
