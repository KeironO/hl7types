"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RQA_I08.GUARANTOR_INSURANCE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.GT1 import GT1
from .RQA_I08_INSURANCE import RQA_I08_INSURANCE

_GT1 = GT1
_RQA_I08_INSURANCE = RQA_I08_INSURANCE


class RQA_I08_GUARANTOR_INSURANCE(BaseModel):
    """HL7 v2 RQA_I08.GUARANTOR_INSURANCE group.

    Attributes:
        GT1 (Optional[List[GT1]]): optional
        INSURANCE (List[RQA_I08_INSURANCE]): required
    """

    GT1: list[_GT1] | None = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: list[_RQA_I08_INSURANCE] = Field(
        default=...,
        title="INSURANCE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
