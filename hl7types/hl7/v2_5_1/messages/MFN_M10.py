"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFN_M10
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.MFN_M10_MF_TEST_BATTERIES import MFN_M10_MF_TEST_BATTERIES
from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

_MFI = MFI
_MFN_M10_MF_TEST_BATTERIES = MFN_M10_MF_TEST_BATTERIES
_MSH = MSH
_SFT = SFT


class MFN_M10(BaseModel):
    """HL7 v2 MFN_M10 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
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
