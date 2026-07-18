"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFD_M01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFA import MFA
from ..segments.MFI import MFI
from ..segments.MSH import MSH

_MFA = MFA
_MFI = MFI
_MSH = MSH


class MFD_M01(HL7Model):
    """HL7 v2 MFD_M01 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        MFI (MFI): MASTER FILE IDENTIFICATION, required
        MFA (Optional[List[MFA]]): MASTER FILE ACKNOWLEDGEMENT, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="MASTER FILE IDENTIFICATION",
    )

    MFA: Optional[List[_MFA]] = Field(
        default=None,
        title="MFA",
        description="MASTER FILE ACKNOWLEDGEMENT",
    )

    model_config = ConfigDict(populate_by_name=True)
