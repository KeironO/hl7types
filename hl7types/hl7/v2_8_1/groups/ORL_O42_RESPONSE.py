"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O42.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .ORL_O42_PATIENT import ORL_O42_PATIENT
from .ORL_O42_SPECIMEN import ORL_O42_SPECIMEN

_ORL_O42_PATIENT = ORL_O42_PATIENT
_ORL_O42_SPECIMEN = ORL_O42_SPECIMEN


class ORL_O42_RESPONSE(HL7Model):
    """HL7 v2 ORL_O42.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORL_O42_PATIENT]): optional
        SPECIMEN (List[ORL_O42_SPECIMEN]): required
    """

    PATIENT: Optional[_ORL_O42_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    SPECIMEN: List[_ORL_O42_SPECIMEN] = Field(
        min_length=1,
        title="SPECIMEN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
