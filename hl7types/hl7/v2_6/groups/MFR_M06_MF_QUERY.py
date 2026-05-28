"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MFR_M06.MF_QUERY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CM0 import CM0
from ..segments.MFE import MFE
from .MFR_M06_MF_PHASE_SCHED_DETAIL import MFR_M06_MF_PHASE_SCHED_DETAIL

_CM0 = CM0
_MFE = MFE
_MFR_M06_MF_PHASE_SCHED_DETAIL = MFR_M06_MF_PHASE_SCHED_DETAIL


class MFR_M06_MF_QUERY(BaseModel):
    """HL7 v2 MFR_M06.MF_QUERY group.

    Attributes:
        MFE (MFE): required
        CM0 (CM0): required
        MF_PHASE_SCHED_DETAIL (Optional[List[MFR_M06_MF_PHASE_SCHED_DETAIL]]): optional
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

    MF_PHASE_SCHED_DETAIL: list[_MFR_M06_MF_PHASE_SCHED_DETAIL] | None = Field(
        default=None,
        title="MF_PHASE_SCHED_DETAIL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
