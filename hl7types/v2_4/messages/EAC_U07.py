"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EAC_U07
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CNS import CNS
from ..segments.ECD import ECD
from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SAC import SAC

_CNS = CNS
_ECD = ECD
_EQU = EQU
_MSH = MSH
_ROL = ROL
_SAC = SAC


class EAC_U07(BaseModel):
    """HL7 v2 EAC_U07 message.

    Attributes:
        MSH (MSH): required
        EQU (EQU): required
        ECD (List[ECD]): required
        SAC (Optional[SAC]): optional
        CNS (Optional[CNS]): optional
        ROL (Optional[ROL]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    EQU: _EQU = Field(
        default=...,
        title="EQU",
        description="Required",
    )

    ECD: List[_ECD] = Field(
        default=...,
        title="ECD",
        description="Required, repeating",
    )

    SAC: Optional[_SAC] = Field(
        default=None,
        title="SAC",
        description="Optional",
    )

    CNS: Optional[_CNS] = Field(
        default=None,
        title="CNS",
        description="Optional",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
