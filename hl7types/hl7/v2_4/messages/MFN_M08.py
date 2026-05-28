"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M08
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MFI import MFI
from ..segments.MSH import MSH

from ..groups.MFN_M08_MF_TEST_NUMERIC import MFN_M08_MF_TEST_NUMERIC

_MFI = MFI
_MFN_M08_MF_TEST_NUMERIC = MFN_M08_MF_TEST_NUMERIC
_MSH = MSH


class MFN_M08(BaseModel):
    """HL7 v2 MFN_M08 message.

    Attributes:
        MSH (MSH): required
        MFI (MFI): required
        MF_TEST_NUMERIC (List[MFN_M08_MF_TEST_NUMERIC]): required
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

    MF_TEST_NUMERIC: List[_MFN_M08_MF_TEST_NUMERIC] = Field(
        default=...,
        title="MF_TEST_NUMERIC",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
