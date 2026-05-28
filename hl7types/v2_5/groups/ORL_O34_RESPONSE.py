"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORL_O34.RESPONSE
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from .ORL_O34_PATIENT import ORL_O34_PATIENT

_ORL_O34_PATIENT = ORL_O34_PATIENT


class ORL_O34_RESPONSE(BaseModel):
    """HL7 v2 ORL_O34.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORL_O34_PATIENT]): optional
    """

    PATIENT: Optional[_ORL_O34_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
