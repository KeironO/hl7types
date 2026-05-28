"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MFN_M11
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.MFN_M11_MF_TEST_CALCULATED import MFN_M11_MF_TEST_CALCULATED

_MFI = MFI
_MFN_M11_MF_TEST_CALCULATED = MFN_M11_MF_TEST_CALCULATED
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M11(BaseModel):
    """HL7 v2 MFN_M11 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MFI (MFI): required
        MF_TEST_CALCULATED (List[MFN_M11_MF_TEST_CALCULATED]): required
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

    MF_TEST_CALCULATED: List[_MFN_M11_MF_TEST_CALCULATED] = Field(
        default=...,
        title="MF_TEST_CALCULATED",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
