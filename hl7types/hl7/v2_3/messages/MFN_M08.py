"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M08
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M08_MF_TEST_NUMERIC import MFN_M08_MF_TEST_NUMERIC

_MFI = MFI
_MFN_M08_MF_TEST_NUMERIC = MFN_M08_MF_TEST_NUMERIC
_MSH = MSH


class MFN_M08(HL7Model):
    """MFN/MFK - Test/Observation (Numeric) master file.

    Attributes:
        MSH (MSH): Message header segment, required
        MFI (MFI): Master file identification segment, required
        MF_TEST_NUMERIC (List[MFN_M08_MF_TEST_NUMERIC]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master file identification segment",
    )

    MF_TEST_NUMERIC: List[_MFN_M08_MF_TEST_NUMERIC] = Field(
        min_length=1,
        title="MF_TEST_NUMERIC",
    )

    model_config = {"populate_by_name": True}
