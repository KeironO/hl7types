"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M07
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M07_MF_CLIN_STUDY_SCHED import MFN_M07_MF_CLIN_STUDY_SCHED

_MFI = MFI
_MFN_M07_MF_CLIN_STUDY_SCHED = MFN_M07_MF_CLIN_STUDY_SCHED
_MSH = MSH


class MFN_M07(BaseModel):
    """HL7 v2 MFN_M07 message.

    Attributes:
        MSH (MSH): required
        MFI (MFI): required
        MF_CLIN_STUDY_SCHED (List[MFN_M07_MF_CLIN_STUDY_SCHED]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF_CLIN_STUDY_SCHED: List[_MFN_M07_MF_CLIN_STUDY_SCHED] = Field(
        default=...,
        title="MF_CLIN_STUDY_SCHED",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
