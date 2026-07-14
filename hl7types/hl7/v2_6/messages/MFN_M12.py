"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MFN_M12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.MFN_M12_MF_OBS_ATTRIBUTES import MFN_M12_MF_OBS_ATTRIBUTES

_MFI = MFI
_MFN_M12_MF_OBS_ATTRIBUTES = MFN_M12_MF_OBS_ATTRIBUTES
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M12(HL7Model):
    """MFN/MFK - Master file notification message (S8.10.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MFI (MFI): Master File Identification, required
        MF_OBS_ATTRIBUTES (List[MFN_M12_MF_OBS_ATTRIBUTES]): required
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

    MF_OBS_ATTRIBUTES: List[_MFN_M12_MF_OBS_ATTRIBUTES] = Field(
        min_length=1,
        title="MF_OBS_ATTRIBUTES",
    )

    model_config = {"populate_by_name": True}
