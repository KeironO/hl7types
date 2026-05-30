"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFN_M01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
    """HL7 v2 MFN_M01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MFI (MFI): required
        MF (List[MFN_M01_MF]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF: List[_MFN_M01_MF] = Field(
        default=...,
        title="MF",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
