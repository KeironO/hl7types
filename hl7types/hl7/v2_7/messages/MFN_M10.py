"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MFN_M10
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.MFN_M10_MF_TEST_BATTERIES import MFN_M10_MF_TEST_BATTERIES
from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MFI = MFI
_MFN_M10_MF_TEST_BATTERIES = MFN_M10_MF_TEST_BATTERIES
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M10(BaseModel):
    """HL7 v2 MFN_M10 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MFI (MFI): required
        MF_TEST_BATTERIES (List[MFN_M10_MF_TEST_BATTERIES]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF_TEST_BATTERIES: list[_MFN_M10_MF_TEST_BATTERIES] = Field(
        default=...,
        title="MF_TEST_BATTERIES",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
