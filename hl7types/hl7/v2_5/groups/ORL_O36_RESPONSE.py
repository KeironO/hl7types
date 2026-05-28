"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORL_O36.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .ORL_O36_PATIENT import ORL_O36_PATIENT

_ORL_O36_PATIENT = ORL_O36_PATIENT


class ORL_O36_RESPONSE(BaseModel):
    """HL7 v2 ORL_O36.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORL_O36_PATIENT]): optional
    """

    PATIENT: _ORL_O36_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
