"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORX_O58.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .ORX_O58_ORDER import ORX_O58_ORDER
from .ORX_O58_PATIENT import ORX_O58_PATIENT

_ORX_O58_ORDER = ORX_O58_ORDER
_ORX_O58_PATIENT = ORX_O58_PATIENT


class ORX_O58_RESPONSE(BaseModel):
    """HL7 v2 ORX_O58.RESPONSE group.

    Attributes:
        PATIENT (Optional[ORX_O58_PATIENT]): optional
        ORDER (List[ORX_O58_ORDER]): required
    """

    PATIENT: Optional[_ORX_O58_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_ORX_O58_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
