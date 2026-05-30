"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_K31.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .RSP_K31_ORDER import RSP_K31_ORDER
from .RSP_K31_PATIENT import RSP_K31_PATIENT

_RSP_K31_ORDER = RSP_K31_ORDER
_RSP_K31_PATIENT = RSP_K31_PATIENT


class RSP_K31_RESPONSE(HL7Model):
    """HL7 v2 RSP_K31.RESPONSE group.

    Attributes:
        PATIENT (Optional[RSP_K31_PATIENT]): optional
        ORDER (List[RSP_K31_ORDER]): required
    """

    PATIENT: Optional[_RSP_K31_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RSP_K31_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
