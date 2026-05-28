"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFN_M09
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M09_MF_TEST_CATEGORICAL import MFN_M09_MF_TEST_CATEGORICAL

_MFI = MFI
_MFN_M09_MF_TEST_CATEGORICAL = MFN_M09_MF_TEST_CATEGORICAL
_MSH = MSH


class MFN_M09(BaseModel):
    """HL7 v2 MFN_M09 message.

    Attributes:
        MSH (MSH): required
        MFI (MFI): required
        MF_TEST_CATEGORICAL (List[MFN_M09_MF_TEST_CATEGORICAL]): required
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

    MF_TEST_CATEGORICAL: List[_MFN_M09_MF_TEST_CATEGORICAL] = Field(
        default=...,
        title="MF_TEST_CATEGORICAL",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
