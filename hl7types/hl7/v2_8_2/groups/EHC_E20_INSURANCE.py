"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EHC_E20.INSURANCE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.IN1 import IN1
from ..segments.IN2 import IN2

_IN1 = IN1
_IN2 = IN2


class EHC_E20_INSURANCE(HL7Model):
    """HL7 v2 EHC_E20.INSURANCE group.

    Attributes:
        IN1 (IN1): required
        IN2 (Optional[IN2]): optional
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

    model_config = {"populate_by_name": True}
