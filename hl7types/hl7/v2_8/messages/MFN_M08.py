"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MFN_M08
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.MFN_M08_MF_TEST_NUMERIC import MFN_M08_MF_TEST_NUMERIC

_MFI = MFI
_MFN_M08_MF_TEST_NUMERIC = MFN_M08_MF_TEST_NUMERIC
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFN_M08(HL7Model):
    """MFN/MFK - Test/observation (numeric) master file (S8.10.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MFI (MFI): Master File Identification, required
        MF_TEST_NUMERIC (List[MFN_M08_MF_TEST_NUMERIC]): required
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

    MF_TEST_NUMERIC: List[_MFN_M08_MF_TEST_NUMERIC] = Field(
        min_length=1,
        title="MF_TEST_NUMERIC",
    )

    model_config = ConfigDict(populate_by_name=True)
