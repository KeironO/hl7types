"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M18
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.MFN_M18_MF_PAYER import MFN_M18_MF_PAYER

_MFI = MFI
_MFN_M18_MF_PAYER = MFN_M18_MF_PAYER
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M18(HL7Model):
    """HL7 v2 MFN_M18 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MFI (MFI): required
        MF_PAYER (List[MFN_M18_MF_PAYER]): required
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Required",
    )

    MF_PAYER: List[_MFN_M18_MF_PAYER] = Field(
        min_length=1,
        title="MF_PAYER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
