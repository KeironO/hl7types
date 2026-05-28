"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFN_M07
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.MFN_M07_MF_CLIN_STUDY_SCHED import MFN_M07_MF_CLIN_STUDY_SCHED
from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

_MFI = MFI
_MFN_M07_MF_CLIN_STUDY_SCHED = MFN_M07_MF_CLIN_STUDY_SCHED
_MSH = MSH
_SFT = SFT


class MFN_M07(BaseModel):
    """HL7 v2 MFN_M07 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MFI (MFI): required
        MF_CLIN_STUDY_SCHED (List[MFN_M07_MF_CLIN_STUDY_SCHED]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF_CLIN_STUDY_SCHED: list[_MFN_M07_MF_CLIN_STUDY_SCHED] = Field(
        default=...,
        title="MF_CLIN_STUDY_SCHED",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
