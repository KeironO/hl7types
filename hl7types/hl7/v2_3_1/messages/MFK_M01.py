"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFK_M01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MFA import MFA
from ..segments.MFI import MFI
from ..segments.MSA import MSA
from ..segments.MSH import MSH

_ERR = ERR
_MFA = MFA
_MFI = MFI
_MSA = MSA
_MSH = MSH


class MFK_M01(HL7Model):
    """MFN/MFK - Master file not otherwise specified (for backward compatibility only).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        ERR (Optional[ERR]): ERR - error segment, optional
        MFI (MFI): MFI - master file identification segment, required
        MFA (Optional[List[MFA]]): MFA - master file acknowledgment segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MSA - message acknowledgment segment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="ERR - error segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="MFI - master file identification segment",
    )

    MFA: Optional[List[_MFA]] = Field(
        default=None,
        title="MFA",
        description="MFA - master file acknowledgment segment",
    )

    model_config = {"populate_by_name": True}
