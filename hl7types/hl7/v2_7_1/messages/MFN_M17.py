"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: MFN_M17
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

from ..groups.MFN_M17_MF_DRG import MFN_M17_MF_DRG

_MFI = MFI
_MFN_M17_MF_DRG = MFN_M17_MF_DRG
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M17(HL7Model):
    """DRG Master File Message (S8.10.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MFI (MFI): Master File Identification, required
        MF_DRG (List[MFN_M17_MF_DRG]): required
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

    MF_DRG: List[_MFN_M17_MF_DRG] = Field(
        min_length=1,
        title="MF_DRG",
    )

    model_config = ConfigDict(populate_by_name=True)
