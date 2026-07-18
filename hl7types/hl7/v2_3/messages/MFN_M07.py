"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M07
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M07_MF_CLIN_STUDY import MFN_M07_MF_CLIN_STUDY

_MFI = MFI
_MFN_M07_MF_CLIN_STUDY = MFN_M07_MF_CLIN_STUDY
_MSH = MSH


class MFN_M07(HL7Model):
    """MFN/MFK - Clinical study without phases but with schedules master file.

    Attributes:
        MSH (MSH): Message header segment, required
        MFI (MFI): Master file identification segment, required
        MF_CLIN_STUDY (List[MFN_M07_MF_CLIN_STUDY]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master file identification segment",
    )

    MF_CLIN_STUDY: List[_MFN_M07_MF_CLIN_STUDY] = Field(
        min_length=1,
        title="MF_CLIN_STUDY",
    )

    model_config = ConfigDict(populate_by_name=True)
