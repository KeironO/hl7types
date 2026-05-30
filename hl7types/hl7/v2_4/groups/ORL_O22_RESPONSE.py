"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORL_O22.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from .ORL_O22_PATIENT import ORL_O22_PATIENT

_ORL_O22_PATIENT = ORL_O22_PATIENT


class ORL_O22_RESPONSE(HL7Model):
    """HL7 v2 ORL_O22.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORL_O22_PATIENT]): optional
    """

    PATIENT: Optional[_ORL_O22_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
