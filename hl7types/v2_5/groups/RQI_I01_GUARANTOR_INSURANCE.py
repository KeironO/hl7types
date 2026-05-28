"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RQI_I01.GUARANTOR_INSURANCE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.GT1 import GT1

from .RQI_I01_INSURANCE import RQI_I01_INSURANCE

_GT1 = GT1
_RQI_I01_INSURANCE = RQI_I01_INSURANCE


class RQI_I01_GUARANTOR_INSURANCE(BaseModel):
    """HL7 v2 RQI_I01.GUARANTOR_INSURANCE group.

    Attributes:
        GT1 (Optional[List[GT1]]): optional
        INSURANCE (List[RQI_I01_INSURANCE]): required
    """

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: List[_RQI_I01_INSURANCE] = Field(
        default=...,
        title="INSURANCE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
