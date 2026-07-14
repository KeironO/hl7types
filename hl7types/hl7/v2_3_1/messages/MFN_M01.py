"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFN_M01
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M01_MF import MFN_M01_MF

_MFI = MFI
_MFN_M01_MF = MFN_M01_MF
_MSH = MSH


class MFN_M01(HL7Model):
    """MFN/MFK - Master file not otherwise specified (for backward compatibility only).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MFI (MFI): MFI - master file identification segment, required
        MF (List[MFN_M01_MF]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="MFI - master file identification segment",
    )

    MF: List[_MFN_M01_MF] = Field(
        min_length=1,
        title="MF",
    )

    model_config = {"populate_by_name": True}
