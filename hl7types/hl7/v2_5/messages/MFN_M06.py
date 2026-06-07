"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFN_M06
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

from ..groups.MFN_M06_MF_CLIN_STUDY import MFN_M06_MF_CLIN_STUDY

_MFI = MFI
_MFN_M06_MF_CLIN_STUDY = MFN_M06_MF_CLIN_STUDY
_MSH = MSH
_SFT = SFT


class MFN_M06(HL7Model):
    """HL7 v2 MFN_M06 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MFI (MFI): required
        MF_CLIN_STUDY (List[MFN_M06_MF_CLIN_STUDY]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Required",
    )

    MF_CLIN_STUDY: List[_MFN_M06_MF_CLIN_STUDY] = Field(
        min_length=1,
        title="MF_CLIN_STUDY",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
