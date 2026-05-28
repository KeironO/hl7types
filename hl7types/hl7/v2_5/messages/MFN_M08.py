"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFN_M08
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.MFN_M08_MF_TEST_NUMERIC import MFN_M08_MF_TEST_NUMERIC
from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

_MFI = MFI
_MFN_M08_MF_TEST_NUMERIC = MFN_M08_MF_TEST_NUMERIC
_MSH = MSH
_SFT = SFT


class MFN_M08(BaseModel):
    """HL7 v2 MFN_M08 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MFI (MFI): required
        MF_TEST_NUMERIC (List[MFN_M08_MF_TEST_NUMERIC]): required
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

    MF_TEST_NUMERIC: list[_MFN_M08_MF_TEST_NUMERIC] = Field(
        default=...,
        title="MF_TEST_NUMERIC",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
