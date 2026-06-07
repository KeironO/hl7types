"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OSR_Q06.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .OSR_Q06_OBSERVATION import OSR_Q06_OBSERVATION
from .OSR_Q06_PATIENT import OSR_Q06_PATIENT

_OSR_Q06_OBSERVATION = OSR_Q06_OBSERVATION
_OSR_Q06_PATIENT = OSR_Q06_PATIENT


class OSR_Q06_RESPONSE(HL7Model):
    """HL7 v2 OSR_Q06.RESPONSE group.

    Attributes:
        PATIENT (Optional[OSR_Q06_PATIENT]): optional
        OBSERVATION (List[OSR_Q06_OBSERVATION]): required
    """

    PATIENT: Optional[_OSR_Q06_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    OBSERVATION: List[_OSR_Q06_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
