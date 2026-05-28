"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RQA_I08.GUARANTOR_INSURANCE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
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

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: List[_RQA_I08_INSURANCE] = Field(
        default=...,
        title="INSURANCE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
