"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFN_M02
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M02_MF_STAFF import MFN_M02_MF_STAFF

_MFI = MFI
_MFN_M02_MF_STAFF = MFN_M02_MF_STAFF
_MSH = MSH


class MFN_M02(HL7Model):
    """HL7 v2 MFN_M02 message.

    Attributes:
        MSH (MSH): required
        MFI (MFI): required
        MF_STAFF (List[MFN_M02_MF_STAFF]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Required",
    )

    MF_STAFF: List[_MFN_M02_MF_STAFF] = Field(
        min_length=1,
        title="MF_STAFF",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
