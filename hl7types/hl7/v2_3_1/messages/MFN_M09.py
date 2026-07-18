"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFN_M09
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M09_MF_TEST_CATEGORICAL import MFN_M09_MF_TEST_CATEGORICAL

_MFI = MFI
_MFN_M09_MF_TEST_CATEGORICAL = MFN_M09_MF_TEST_CATEGORICAL
_MSH = MSH


class MFN_M09(HL7Model):
    """MFN/MFK - Test/Observation (Categorical) master file.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MFI (MFI): MFI - master file identification segment, required
        MF_TEST_CATEGORICAL (List[MFN_M09_MF_TEST_CATEGORICAL]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="MFI - master file identification segment",
    )

    MF_TEST_CATEGORICAL: List[_MFN_M09_MF_TEST_CATEGORICAL] = Field(
        min_length=1,
        title="MF_TEST_CATEGORICAL",
    )

    model_config = ConfigDict(populate_by_name=True)
