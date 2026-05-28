"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: TCU_U10
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.TCU_U10_TEST_CONFIGURATION import TCU_U10_TEST_CONFIGURATION

_EQU = EQU
_MSH = MSH
_SFT = SFT
_TCU_U10_TEST_CONFIGURATION = TCU_U10_TEST_CONFIGURATION
_UAC = UAC


class TCU_U10(BaseModel):
    """HL7 v2 TCU_U10 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EQU (EQU): required
        TEST_CONFIGURATION (List[TCU_U10_TEST_CONFIGURATION]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    EQU: _EQU = Field(
        default=...,
        title="EQU",
        description="Required",
    )

    TEST_CONFIGURATION: List[_TCU_U10_TEST_CONFIGURATION] = Field(
        default=...,
        title="TEST_CONFIGURATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
