"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MFN_M06.MF_PHASE_SCHED_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CM1 import CM1
from ..segments.CM2 import CM2

_CM1 = CM1
_CM2 = CM2


class MFN_M06_MF_PHASE_SCHED_DETAIL(HL7Model):
    """HL7 v2 MFN_M06.MF_PHASE_SCHED_DETAIL group.

    Attributes:
        CM1 (CM1): Clinical Study Phase Master, required
        CM2 (Optional[List[CM2]]): Clinical Study Schedule Master, optional
    """

    CM1: _CM1 = Field(
        title="CM1",
        description="Clinical Study Phase Master",
    )

    CM2: Optional[List[_CM2]] = Field(
        default=None,
        title="CM2",
        description="Clinical Study Schedule Master",
    )

    model_config = ConfigDict(populate_by_name=True)
