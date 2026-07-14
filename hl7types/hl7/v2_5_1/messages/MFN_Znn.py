"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFN_Znn
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

from ..groups.MFN_Znn_MF_SITE_DEFINED import MFN_Znn_MF_SITE_DEFINED

_MFI = MFI
_MFN_Znn_MF_SITE_DEFINED = MFN_Znn_MF_SITE_DEFINED
_MSH = MSH
_SFT = SFT


class MFN_Znn(HL7Model):
    """HL7 v2 MFN_Znn message.

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        MFI (MFI): Master File Identification, required
        MF_SITE_DEFINED (List[MFN_Znn_MF_SITE_DEFINED]): required
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

    MF_SITE_DEFINED: List[_MFN_Znn_MF_SITE_DEFINED] = Field(
        min_length=1,
        title="MF_SITE_DEFINED",
    )

    model_config = {"populate_by_name": True}
