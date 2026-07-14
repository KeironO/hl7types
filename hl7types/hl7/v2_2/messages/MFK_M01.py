"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
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
    """HL7 v2 MFK_M01 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        MSA (MSA): MESSAGE ACKNOWLEDGMENT, required
        ERR (Optional[ERR]): ERROR, optional
        MFI (MFI): MASTER FILE IDENTIFICATION, required
        MFA (Optional[List[MFA]]): MASTER FILE ACKNOWLEDGEMENT, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MESSAGE ACKNOWLEDGMENT",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="ERROR",
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

    model_config = {"populate_by_name": True}
