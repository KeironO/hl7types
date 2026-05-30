"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M06
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M06_MF_CDM import MFN_M06_MF_CDM

_MFI = MFI
_MFN_M06_MF_CDM = MFN_M06_MF_CDM
_MSH = MSH


class MFN_M06(HL7Model):
    """HL7 v2 MFN_M06 message.

    Attributes:
        MSH (MSH): required
        MFI (MFI): required
        MF_CDM (List[MFN_M06_MF_CDM]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF_CDM: List[_MFN_M06_MF_CDM] = Field(
        default=...,
        title="MF_CDM",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
