"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M03
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M03_MF_TEST import MFN_M03_MF_TEST

_MFI = MFI
_MFN_M03_MF_TEST = MFN_M03_MF_TEST
_MSH = MSH


class MFN_M03(HL7Model):
    """MFN/MFK - Master file - Test/Observation (for backward compatibility only) (S8).

    Attributes:
        MSH (MSH): Message Header, required
        MFI (MFI): Master File Identification, required
        MF_TEST (List[MFN_M03_MF_TEST]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
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
