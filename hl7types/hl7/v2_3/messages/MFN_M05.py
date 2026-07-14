"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M05
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M05_MF_LOCATION import MFN_M05_MF_LOCATION

_MFI = MFI
_MFN_M05_MF_LOCATION = MFN_M05_MF_LOCATION
_MSH = MSH


class MFN_M05(HL7Model):
    """MFN/MFK - Patient location master file.

    Attributes:
        MSH (MSH): Message header segment, required
        MFI (MFI): Master file identification segment, required
        MF_LOCATION (List[MFN_M05_MF_LOCATION]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master file identification segment",
    )

    MF_LOCATION: List[_MFN_M05_MF_LOCATION] = Field(
        min_length=1,
        title="MF_LOCATION",
    )

    model_config = {"populate_by_name": True}
