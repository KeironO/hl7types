"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OML_O21.INSURANCE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.IN1 import IN1
from ..segments.IN2 import IN2
from ..segments.IN3 import IN3

_IN1 = IN1
_IN2 = IN2
_IN3 = IN3


class OML_O21_INSURANCE(BaseModel):
    """HL7 v2 OML_O21.INSURANCE group.

    Attributes:
        IN1 (IN1): required
        IN2 (Optional[IN2]): optional
        IN3 (Optional[IN3]): optional
    """

    IN1: _IN1 = Field(
        default=...,
        title="IN1",
        description="Required",
    )

    IN2: _IN2 | None = Field(
        default=None,
        title="IN2",
        description="Optional",
    )

    IN3: _IN3 | None = Field(
        default=None,
        title="IN3",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
