"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFN_M03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

from ..groups.MFN_M03_MF_TEST import MFN_M03_MF_TEST

_MFI = MFI
_MFN_M03_MF_TEST = MFN_M03_MF_TEST
_MSH = MSH
_SFT = SFT


class MFN_M03(HL7Model):
    """MFN/MFK - Master file - test/observation (for backward compatibility only) (S8.10.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        MFI (MFI): Master File Identification, required
        MF_TEST (List[MFN_M03_MF_TEST]): required
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

    MFI: _MFI = Field(
        title="MFI",
        description="Master File Identification",
    )

    MF_TEST: List[_MFN_M03_MF_TEST] = Field(
        min_length=1,
        title="MF_TEST",
    )

    model_config = {"populate_by_name": True}
