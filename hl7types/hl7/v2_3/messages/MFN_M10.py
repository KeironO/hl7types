"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M10
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M10_MF_TEST_BATTERIES import MFN_M10_MF_TEST_BATTERIES

_MFI = MFI
_MFN_M10_MF_TEST_BATTERIES = MFN_M10_MF_TEST_BATTERIES
_MSH = MSH


class MFN_M10(HL7Model):
    """HL7 v2 MFN_M10 message.

    Attributes:
        MSH (MSH): required
        MFI (MFI): required
        MF_TEST_BATTERIES (List[MFN_M10_MF_TEST_BATTERIES]): required
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

    MF_TEST_BATTERIES: List[_MFN_M10_MF_TEST_BATTERIES] = Field(
        default=...,
        title="MF_TEST_BATTERIES",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
