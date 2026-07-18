"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFN_M01
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M01_MF import MFN_M01_MF

_MFI = MFI
_MFN_M01_MF = MFN_M01_MF
_MSH = MSH


class MFN_M01(HL7Model):
    """HL7 v2 MFN_M01 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        MFI (MFI): MASTER FILE IDENTIFICATION, required
        MF (List[MFN_M01_MF]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="MASTER FILE IDENTIFICATION",
    )

    MF: List[_MFN_M01_MF] = Field(
        min_length=1,
        title="MF",
    )

    model_config = ConfigDict(populate_by_name=True)
