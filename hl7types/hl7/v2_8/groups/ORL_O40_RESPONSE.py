"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORL_O40.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from .ORL_O40_PATIENT import ORL_O40_PATIENT

_ORL_O40_PATIENT = ORL_O40_PATIENT


class ORL_O40_RESPONSE(HL7Model):
    """HL7 v2 ORL_O40.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORL_O40_PATIENT]): optional
    """

    PATIENT: Optional[_ORL_O40_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
