"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: TCU_U10
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT

from ..groups.TCU_U10_TEST_CONFIGURATION import TCU_U10_TEST_CONFIGURATION

_EQU = EQU
_MSH = MSH
_ROL = ROL
_SFT = SFT
_TCU_U10_TEST_CONFIGURATION = TCU_U10_TEST_CONFIGURATION


class TCU_U10(BaseModel):
    """HL7 v2 TCU_U10 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EQU (EQU): required
        TEST_CONFIGURATION (List[TCU_U10_TEST_CONFIGURATION]): required
        ROL (Optional[ROL]): optional
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

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
