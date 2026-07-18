"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M04
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M04_MF_CDM import MFN_M04_MF_CDM

_MFI = MFI
_MFN_M04_MF_CDM = MFN_M04_MF_CDM
_MSH = MSH


class MFN_M04(HL7Model):
    """MFN/MFK - Master files charge description (S8).

    Attributes:
        MSH (MSH): Message Header, required
        MFI (MFI): Master File Identification, required
        MF_CDM (List[MFN_M04_MF_CDM]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master File Identification",
    )

    MF_CDM: List[_MFN_M04_MF_CDM] = Field(
        min_length=1,
        title="MF_CDM",
    )

    model_config = ConfigDict(populate_by_name=True)
