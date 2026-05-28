"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z90.QUERY_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .RSP_Z90_COMMON_ORDER import RSP_Z90_COMMON_ORDER
from .RSP_Z90_PATIENT import RSP_Z90_PATIENT

_RSP_Z90_COMMON_ORDER = RSP_Z90_COMMON_ORDER
_RSP_Z90_PATIENT = RSP_Z90_PATIENT


class RSP_Z90_QUERY_RESPONSE(BaseModel):
    """HL7 v2 RSP_Z90.QUERY_RESPONSE group.

    Attributes:
        PATIENT (Optional[RSP_Z90_PATIENT]): optional
        COMMON_ORDER (List[RSP_Z90_COMMON_ORDER]): required
    """

    PATIENT: Optional[_RSP_Z90_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    COMMON_ORDER: List[_RSP_Z90_COMMON_ORDER] = Field(
        default=...,
        title="COMMON_ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
