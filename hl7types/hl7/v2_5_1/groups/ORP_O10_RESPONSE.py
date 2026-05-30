"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORP_O10.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .ORP_O10_ORDER import ORP_O10_ORDER
from .ORP_O10_PATIENT import ORP_O10_PATIENT

_ORP_O10_ORDER = ORP_O10_ORDER
_ORP_O10_PATIENT = ORP_O10_PATIENT


class ORP_O10_RESPONSE(HL7Model):
    """HL7 v2 ORP_O10.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORP_O10_PATIENT]): optional
        ORDER (List[ORP_O10_ORDER]): required
    """

    PATIENT: Optional[_ORP_O10_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_ORP_O10_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
