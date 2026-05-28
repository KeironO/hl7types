"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORB_O28.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .ORB_O28_PATIENT import ORB_O28_PATIENT

_ORB_O28_PATIENT = ORB_O28_PATIENT


class ORB_O28_RESPONSE(BaseModel):
    """HL7 v2 ORB_O28.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORB_O28_PATIENT]): optional
    """

    PATIENT: _ORB_O28_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
