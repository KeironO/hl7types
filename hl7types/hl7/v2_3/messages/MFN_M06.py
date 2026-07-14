"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M06
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M06_MF_CDM import MFN_M06_MF_CDM

_MFI = MFI
_MFN_M06_MF_CDM = MFN_M06_MF_CDM
_MSH = MSH


class MFN_M06(HL7Model):
    """MFN/MFK - Clinical study master file.

    Attributes:
        MSH (MSH): Message header segment, required
        MFI (MFI): Master file identification segment, required
        MF_CDM (List[MFN_M06_MF_CDM]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master file identification segment",
    )

    MF_CDM: List[_MFN_M06_MF_CDM] = Field(
        min_length=1,
        title="MF_CDM",
    )

    model_config = {"populate_by_name": True}
