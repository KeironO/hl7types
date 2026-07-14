"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
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
    """MFN/MFK - Master file - Staff Practioner.

    Attributes:
        MSH (MSH): Message header segment, required
        MFI (MFI): Master file identification segment, required
        MF_STAFF (List[MFN_M02_MF_STAFF]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master file identification segment",
    )

    MF_STAFF: List[_MFN_M02_MF_STAFF] = Field(
        min_length=1,
        title="MF_STAFF",
    )

    model_config = {"populate_by_name": True}
