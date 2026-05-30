"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O43.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .ORL_O43_PATIENT import ORL_O43_PATIENT
from .ORL_O43_SPECIMEN import ORL_O43_SPECIMEN

_ORL_O43_PATIENT = ORL_O43_PATIENT
_ORL_O43_SPECIMEN = ORL_O43_SPECIMEN


class ORL_O43_RESPONSE(HL7Model):
    """HL7 v2 ORL_O43.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORL_O43_PATIENT]): optional
        SPECIMEN (List[ORL_O43_SPECIMEN]): required
    """

    PATIENT: Optional[_ORL_O43_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    SPECIMEN: List[_ORL_O43_SPECIMEN] = Field(
        default=...,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
