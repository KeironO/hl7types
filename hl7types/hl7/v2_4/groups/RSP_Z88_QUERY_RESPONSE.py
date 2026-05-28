"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z88.QUERY_RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .RSP_Z88_PATIENT import RSP_Z88_PATIENT

_RSP_Z88_PATIENT = RSP_Z88_PATIENT


class RSP_Z88_QUERY_RESPONSE(BaseModel):
    """HL7 v2 RSP_Z88.QUERY_RESPONSE group.

    Attributes:
        PATIENT (Optional[RSP_Z88_PATIENT]): optional
    """

    PATIENT: _RSP_Z88_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
