"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.MFN_M04_MF_CDM import MFN_M04_MF_CDM

_MFI = MFI
_MFN_M04_MF_CDM = MFN_M04_MF_CDM
_MSH = MSH
_NTE = NTE
_SFT = SFT
_UAC = UAC


class MFN_M04(HL7Model):
    """MFN/MFK - Master files charge description (S8.10.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MFI (MFI): Master File Identification, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        MF_CDM (List[MFN_M04_MF_CDM]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master File Identification",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    MF_CDM: List[_MFN_M04_MF_CDM] = Field(
        min_length=1,
        title="MF_CDM",
    )

    model_config = ConfigDict(populate_by_name=True)
