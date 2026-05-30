"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: BRP_O30.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from .BRP_O30_PATIENT import BRP_O30_PATIENT

_BRP_O30_PATIENT = BRP_O30_PATIENT


class BRP_O30_RESPONSE(HL7Model):
    """HL7 v2 BRP_O30.RESPONSE group.

    Attributes:
        PATIENT (Optional[BRP_O30_PATIENT]): optional
    """

    PATIENT: Optional[_BRP_O30_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
