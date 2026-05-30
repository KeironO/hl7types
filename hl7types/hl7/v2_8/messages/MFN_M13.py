"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MFN_M13
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE
from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MFE = MFE
_MFI = MFI
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M13(HL7Model):
    """HL7 v2 MFN_M13 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MFI (MFI): required
        MFE (List[MFE]): required
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MFE: List[_MFE] = Field(
        default=...,
        title="MFE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
