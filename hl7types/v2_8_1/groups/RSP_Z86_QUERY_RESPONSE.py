"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_Z86.QUERY_RESPONSE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .RSP_Z86_COMMON_ORDER import RSP_Z86_COMMON_ORDER
from .RSP_Z86_PATIENT import RSP_Z86_PATIENT

_RSP_Z86_COMMON_ORDER = RSP_Z86_COMMON_ORDER
_RSP_Z86_PATIENT = RSP_Z86_PATIENT


class RSP_Z86_QUERY_RESPONSE(BaseModel):
    """HL7 v2 RSP_Z86.QUERY_RESPONSE group.

    Attributes:
        PATIENT (Optional[RSP_Z86_PATIENT]): optional
        COMMON_ORDER (List[RSP_Z86_COMMON_ORDER]): required
    """

    PATIENT: Optional[_RSP_Z86_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    COMMON_ORDER: List[_RSP_Z86_COMMON_ORDER] = Field(
        default=...,
        title="COMMON_ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
