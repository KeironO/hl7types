"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFK_M01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
    """MFN/MFK - Master file not otherwise specified (for backward compatibility only) (S8).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        MFI (MFI): Master File Identification, required
        MFA (Optional[List[MFA]]): Master File Acknowledgment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master File Identification",
    )

    MFA: Optional[List[_MFA]] = Field(
        default=None,
        title="MFA",
        description="Master File Acknowledgment",
    )

    model_config = ConfigDict(populate_by_name=True)
