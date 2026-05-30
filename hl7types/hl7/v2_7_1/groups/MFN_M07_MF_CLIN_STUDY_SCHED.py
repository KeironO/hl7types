"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: MFN_M07.MF_CLIN_STUDY_SCHED
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CM0 import CM0
from ..segments.CM2 import CM2
from ..segments.MFE import MFE

_CM0 = CM0
_CM2 = CM2
_MFE = MFE


class MFN_M07_MF_CLIN_STUDY_SCHED(HL7Model):
    """HL7 v2 MFN_M07.MF_CLIN_STUDY_SCHED group.

    Attributes:
        MFE (MFE): required
        CM0 (CM0): required
        CM2 (Optional[List[CM2]]): optional
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

    CM2: Optional[List[_CM2]] = Field(
        default=None,
        title="CM2",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
