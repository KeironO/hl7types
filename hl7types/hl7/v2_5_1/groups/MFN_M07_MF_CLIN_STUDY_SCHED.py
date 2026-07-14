"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
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
        MFE (MFE): Master File Entry, required
        CM0 (CM0): Clinical Study Master, required
        CM2 (Optional[List[CM2]]): Clinical Study Schedule Master, optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    CM0: _CM0 = Field(
        title="CM0",
        description="Clinical Study Master",
    )

    CM2: Optional[List[_CM2]] = Field(
        default=None,
        title="CM2",
        description="Clinical Study Schedule Master",
    )

    model_config = {"populate_by_name": True}
