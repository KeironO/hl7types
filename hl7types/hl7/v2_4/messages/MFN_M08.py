"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M08
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M08_MF_TEST_NUMERIC import MFN_M08_MF_TEST_NUMERIC

_MFI = MFI
_MFN_M08_MF_TEST_NUMERIC = MFN_M08_MF_TEST_NUMERIC
_MSH = MSH


class MFN_M08(HL7Model):
    """MFN/MFK - Test/observation (Numeric) master file (S8).

    Attributes:
        MSH (MSH): Message Header, required
        MFI (MFI): Master File Identification, required
        MF_TEST_NUMERIC (List[MFN_M08_MF_TEST_NUMERIC]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
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
