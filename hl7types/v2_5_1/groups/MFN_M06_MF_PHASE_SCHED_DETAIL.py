"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFN_M06.MF_PHASE_SCHED_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CM1 import CM1
from ..segments.CM2 import CM2

_CM1 = CM1
_CM2 = CM2


class MFN_M06_MF_PHASE_SCHED_DETAIL(BaseModel):
    """HL7 v2 MFN_M06.MF_PHASE_SCHED_DETAIL group.

    Attributes:
        CM1 (CM1): required
        CM2 (Optional[List[CM2]]): optional
    """

    CM1: _CM1 = Field(
        default=...,
        title="CM1",
        description="Required",
    )

    CM2: Optional[List[_CM2]] = Field(
        default=None,
        title="CM2",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
