"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.INSURANCE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.IN1 import IN1
from ..segments.IN2 import IN2
from ..segments.IN3 import IN3

_IN1 = IN1
_IN2 = IN2
_IN3 = IN3


class CCR_I16_INSURANCE(HL7Model):
    """HL7 v2 CCR_I16.INSURANCE group.

    Attributes:
        IN1 (IN1): required
        IN2 (Optional[IN2]): optional
        IN3 (Optional[IN3]): optional
    """

    IN1: _IN1 = Field(
        title="IN1",
        description="Required",
    )

    IN2: Optional[_IN2] = Field(
        default=None,
        title="IN2",
        description="Optional",
    )

    IN3: Optional[_IN3] = Field(
        default=None,
        title="IN3",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
