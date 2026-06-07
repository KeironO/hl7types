"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RSP_Z88.QUERY_RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .RSP_Z88_COMMON_ORDER import RSP_Z88_COMMON_ORDER
from .RSP_Z88_PATIENT import RSP_Z88_PATIENT

_RSP_Z88_COMMON_ORDER = RSP_Z88_COMMON_ORDER
_RSP_Z88_PATIENT = RSP_Z88_PATIENT


class RSP_Z88_QUERY_RESPONSE(HL7Model):
    """HL7 v2 RSP_Z88.QUERY_RESPONSE group.

    Attributes:
        PATIENT (Optional[RSP_Z88_PATIENT]): optional
        COMMON_ORDER (List[RSP_Z88_COMMON_ORDER]): required
    """

    PATIENT: Optional[_RSP_Z88_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    COMMON_ORDER: List[_RSP_Z88_COMMON_ORDER] = Field(
        min_length=1,
        title="COMMON_ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
