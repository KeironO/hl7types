"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFN_M10
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT

from ..groups.MFN_M10_MF_TEST_BATTERIES import MFN_M10_MF_TEST_BATTERIES

_MFI = MFI
_MFN_M10_MF_TEST_BATTERIES = MFN_M10_MF_TEST_BATTERIES
_MSH = MSH
_SFT = SFT


class MFN_M10(HL7Model):
    """MFN/MFK - Test /observation batteries master file (S8.4.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        MFI (MFI): Master File Identification, required
        MF_TEST_BATTERIES (List[MFN_M10_MF_TEST_BATTERIES]): required
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

    MF_TEST_BATTERIES: List[_MFN_M10_MF_TEST_BATTERIES] = Field(
        min_length=1,
        title="MF_TEST_BATTERIES",
    )

    model_config = {"populate_by_name": True}
