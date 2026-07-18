"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MFN_M01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

from ..groups.MFN_M01_MF import MFN_M01_MF

_MFI = MFI
_MFN_M01_MF = MFN_M01_MF
_MSH = MSH
_SFT = SFT


class MFN_M01(HL7Model):
    """MFN/MFK - Master file not otherwise specified (for backward compatibility only) (S8.10.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        MFI (MFI): Master File Identification, required
        MF (List[MFN_M01_MF]): required
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

    MFI: _MFI = Field(
        title="MFI",
        description="Master File Identification",
    )

    MF: List[_MFN_M01_MF] = Field(
        min_length=1,
        title="MF",
    )

    model_config = ConfigDict(populate_by_name=True)
