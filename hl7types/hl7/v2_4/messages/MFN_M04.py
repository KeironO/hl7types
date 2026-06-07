"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M04
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M04_MF_CDM import MFN_M04_MF_CDM

_MFI = MFI
_MFN_M04_MF_CDM = MFN_M04_MF_CDM
_MSH = MSH


class MFN_M04(HL7Model):
    """HL7 v2 MFN_M04 message.

    Attributes:
        MSH (MSH): required
        MFI (MFI): required
        MF_CDM (List[MFN_M04_MF_CDM]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Required",
    )

    MF_CDM: List[_MFN_M04_MF_CDM] = Field(
        min_length=1,
        title="MF_CDM",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
