"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MFN_M06
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.MFN_M06_MF_CLIN_STUDY import MFN_M06_MF_CLIN_STUDY

_MFI = MFI
_MFN_M06_MF_CLIN_STUDY = MFN_M06_MF_CLIN_STUDY
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M06(HL7Model):
    """MFN/MFK - Clinical study with phases and schedules master file (S8.10.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MFI (MFI): Master File Identification, required
        MF_CLIN_STUDY (List[MFN_M06_MF_CLIN_STUDY]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master File Identification",
    )

    MF_CLIN_STUDY: List[_MFN_M06_MF_CLIN_STUDY] = Field(
        min_length=1,
        title="MF_CLIN_STUDY",
    )

    model_config = ConfigDict(populate_by_name=True)
