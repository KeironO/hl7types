"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFN_M02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.MFN_M02_MF_STAFF import MFN_M02_MF_STAFF
from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

_MFI = MFI
_MFN_M02_MF_STAFF = MFN_M02_MF_STAFF
_MSH = MSH
_SFT = SFT


class MFN_M02(BaseModel):
    """HL7 v2 MFN_M02 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MFI (MFI): required
        MF_STAFF (List[MFN_M02_MF_STAFF]): required
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

    MF_STAFF: list[_MFN_M02_MF_STAFF] = Field(
        default=...,
        title="MF_STAFF",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
