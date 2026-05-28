"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PIN_I07.GUARANTOR_INSURANCE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.GT1 import GT1
from .PIN_I07_INSURANCE import PIN_I07_INSURANCE

_GT1 = GT1
_PIN_I07_INSURANCE = PIN_I07_INSURANCE


class PIN_I07_GUARANTOR_INSURANCE(BaseModel):
    """HL7 v2 PIN_I07.GUARANTOR_INSURANCE group.

    Attributes:
        GT1 (Optional[List[GT1]]): optional
        INSURANCE (List[PIN_I07_INSURANCE]): required
    """

    GT1: list[_GT1] | None = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: list[_PIN_I07_INSURANCE] = Field(
        default=...,
        title="INSURANCE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
