"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RPA_I08.INSURANCE
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.IN1 import IN1
from ..segments.IN2 import IN2
from ..segments.IN3 import IN3

_IN1 = IN1
_IN2 = IN2
_IN3 = IN3


class RPA_I08_INSURANCE(HL7Model):
    """HL7 v2 RPA_I08.INSURANCE group.

    Attributes:
        IN1 (IN1): Insurance, required
        IN2 (Optional[IN2]): Insurance Additional Information, optional
        IN3 (Optional[IN3]): Insurance Additional Information, Certification, optional
    """

    IN1: _IN1 = Field(
        title="IN1",
        description="Insurance",
    )

    IN2: Optional[_IN2] = Field(
        default=None,
        title="IN2",
        description="Insurance Additional Information",
    )

    IN3: Optional[_IN3] = Field(
        default=None,
        title="IN3",
        description="Insurance Additional Information, Certification",
    )

    model_config = ConfigDict(populate_by_name=True)
