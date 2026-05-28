"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M05
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.MFN_M05_MF_LOCATION import MFN_M05_MF_LOCATION
from ..segments.MFI import MFI
from ..segments.MSH import MSH

_MFI = MFI
_MFN_M05_MF_LOCATION = MFN_M05_MF_LOCATION
_MSH = MSH


class MFN_M05(BaseModel):
    """HL7 v2 MFN_M05 message.

    Attributes:
        MSH (MSH): required
        MFI (MFI): required
        MF_LOCATION (List[MFN_M05_MF_LOCATION]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF_LOCATION: list[_MFN_M05_MF_LOCATION] = Field(
        default=...,
        title="MF_LOCATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
