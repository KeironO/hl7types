"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M07
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M07_MF_CLIN_STUDY import MFN_M07_MF_CLIN_STUDY

_MFI = MFI
_MFN_M07_MF_CLIN_STUDY = MFN_M07_MF_CLIN_STUDY
_MSH = MSH


class MFN_M07(HL7Model):
    """HL7 v2 MFN_M07 message.

    Attributes:
        MSH (MSH): required
        MFI (MFI): required
        MF_CLIN_STUDY (List[MFN_M07_MF_CLIN_STUDY]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Required",
    )

    MF_CLIN_STUDY: List[_MFN_M07_MF_CLIN_STUDY] = Field(
        min_length=1,
        title="MF_CLIN_STUDY",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
