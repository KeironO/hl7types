"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFN_M11
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

from ..groups.MFN_M11_MF_TEST_CALCULATED import MFN_M11_MF_TEST_CALCULATED

_MFI = MFI
_MFN_M11_MF_TEST_CALCULATED = MFN_M11_MF_TEST_CALCULATED
_MSH = MSH
_SFT = SFT


class MFN_M11(HL7Model):
    """HL7 v2 MFN_M11 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MFI (MFI): required
        MF_TEST_CALCULATED (List[MFN_M11_MF_TEST_CALCULATED]): required
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

    MFI: _MFI = Field(
        title="MFI",
        description="Required",
    )

    MF_TEST_CALCULATED: List[_MFN_M11_MF_TEST_CALCULATED] = Field(
        min_length=1,
        title="MF_TEST_CALCULATED",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
