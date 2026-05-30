"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORL_O36.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from .ORL_O36_PATIENT import ORL_O36_PATIENT

_ORL_O36_PATIENT = ORL_O36_PATIENT


class ORL_O36_RESPONSE(HL7Model):
    """HL7 v2 ORL_O36.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORL_O36_PATIENT]): optional
    """

    PATIENT: Optional[_ORL_O36_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
