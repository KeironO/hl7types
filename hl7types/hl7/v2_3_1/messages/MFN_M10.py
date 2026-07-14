"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFN_M10
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M10_MF_TEST_BATTERIES import MFN_M10_MF_TEST_BATTERIES

_MFI = MFI
_MFN_M10_MF_TEST_BATTERIES = MFN_M10_MF_TEST_BATTERIES
_MSH = MSH


class MFN_M10(HL7Model):
    """MFN/MFK - Test /observation batteries master file.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MFI (MFI): MFI - master file identification segment, required
        MF_TEST_BATTERIES (List[MFN_M10_MF_TEST_BATTERIES]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="MFI - master file identification segment",
    )

    MF_TEST_BATTERIES: List[_MFN_M10_MF_TEST_BATTERIES] = Field(
        min_length=1,
        title="MF_TEST_BATTERIES",
    )

    model_config = {"populate_by_name": True}
