"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RPI_I04.GUARANTOR_INSURANCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GT1 import GT1

from .RPI_I04_INSURANCE import RPI_I04_INSURANCE

_GT1 = GT1
_RPI_I04_INSURANCE = RPI_I04_INSURANCE


class RPI_I04_GUARANTOR_INSURANCE(HL7Model):
    """HL7 v2 RPI_I04.GUARANTOR_INSURANCE group.

    Attributes:
        GT1 (Optional[List[GT1]]): optional
        INSURANCE (List[RPI_I04_INSURANCE]): required
    """

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: List[_RPI_I04_INSURANCE] = Field(
        min_length=1,
        title="INSURANCE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
