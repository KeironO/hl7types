"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRD_O02.PATIENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .RRD_O02_ORDER import RRD_O02_ORDER
from .RRD_O02_RESPONSE import RRD_O02_RESPONSE

_RRD_O02_ORDER = RRD_O02_ORDER
_RRD_O02_RESPONSE = RRD_O02_RESPONSE


class RRD_O02_PATIENT(BaseModel):
    """HL7 v2 RRD_O02.PATIENT group.

    Attributes:
        RESPONSE (Optional[RRD_O02_RESPONSE]): optional
        ORDER (List[RRD_O02_ORDER]): required
    """

    RESPONSE: Optional[_RRD_O02_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
        description="Optional",
    )

    ORDER: List[_RRD_O02_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
