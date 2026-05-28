"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O41.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .ORL_O41_ORDER import ORL_O41_ORDER
from .ORL_O41_PATIENT import ORL_O41_PATIENT

_ORL_O41_ORDER = ORL_O41_ORDER
_ORL_O41_PATIENT = ORL_O41_PATIENT


class ORL_O41_RESPONSE(BaseModel):
    """HL7 v2 ORL_O41.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORL_O41_PATIENT]): optional
        ORDER (Optional[List[ORL_O41_ORDER]]): optional
    """

    PATIENT: _ORL_O41_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_ORL_O41_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
