"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M07.MF_CLIN_STUDY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CM0 import CM0
from ..segments.MFE import MFE
from .MFN_M07_MF_PHASE_SCHED_DETAIL import MFN_M07_MF_PHASE_SCHED_DETAIL

_CM0 = CM0
_MFE = MFE
_MFN_M07_MF_PHASE_SCHED_DETAIL = MFN_M07_MF_PHASE_SCHED_DETAIL


class MFN_M07_MF_CLIN_STUDY(BaseModel):
    """HL7 v2 MFN_M07.MF_CLIN_STUDY group.

    Attributes:
        MFE (MFE): required
        CM0 (CM0): required
        MF_PHASE_SCHED_DETAIL (Optional[List[MFN_M07_MF_PHASE_SCHED_DETAIL]]): optional
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    CM0: _CM0 = Field(
        default=...,
        title="CM0",
        description="Required",
    )

    MF_PHASE_SCHED_DETAIL: list[_MFN_M07_MF_PHASE_SCHED_DETAIL] | None = Field(
        default=None,
        title="MF_PHASE_SCHED_DETAIL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
