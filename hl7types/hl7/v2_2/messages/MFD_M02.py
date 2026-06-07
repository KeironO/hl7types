"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFD_M02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFA import MFA
from ..segments.MFI import MFI
from ..segments.MSH import MSH

_MFA = MFA
_MFI = MFI
_MSH = MSH


class MFD_M02(HL7Model):
    """HL7 v2 MFD_M02 message.

    Attributes:
        MSH (MSH): required
        MFI (MFI): required
        MFA (Optional[List[MFA]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Required",
    )

    MFA: Optional[List[_MFA]] = Field(
        default=None,
        title="MFA",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
