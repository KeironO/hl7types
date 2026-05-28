"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFK_M02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.MFA import MFA
from ..segments.MFI import MFI
from ..segments.MSA import MSA
from ..segments.MSH import MSH

_MFA = MFA
_MFI = MFI
_MSA = MSA
_MSH = MSH


class MFK_M02(BaseModel):
    """HL7 v2 MFK_M02 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        MFI (MFI): required
        MFA (Optional[List[MFA]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MFA: list[_MFA] | None = Field(
        default=None,
        title="MFA",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
