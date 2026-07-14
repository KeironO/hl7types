"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFK_M01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFA import MFA
from ..segments.MFI import MFI
from ..segments.MSA import MSA
from ..segments.MSH import MSH

_MFA = MFA
_MFI = MFI
_MSA = MSA
_MSH = MSH


class MFK_M01(HL7Model):
    """MFN/MFK - Master file not otherwise specified (for backward comp.only).

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        MFI (MFI): Master file identification segment, required
        MFA (Optional[List[MFA]]): Master file acknowledgement segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message acknowledgement segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master file identification segment",
    )

    MFA: Optional[List[_MFA]] = Field(
        default=None,
        title="MFA",
        description="Master file acknowledgement segment",
    )

    model_config = {"populate_by_name": True}
