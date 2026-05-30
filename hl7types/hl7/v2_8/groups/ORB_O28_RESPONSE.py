"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORB_O28.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from .ORB_O28_PATIENT import ORB_O28_PATIENT

_ORB_O28_PATIENT = ORB_O28_PATIENT


class ORB_O28_RESPONSE(HL7Model):
    """HL7 v2 ORB_O28.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORB_O28_PATIENT]): optional
    """

    PATIENT: Optional[_ORB_O28_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
