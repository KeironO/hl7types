"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EAC_U07
Type: Message
"""

from __future__ import annotations

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

    ECD: list[_ECD] = Field(
        default=...,
        title="ECD",
        description="Required, repeating",
    )

    SAC: _SAC | None = Field(
        default=None,
        title="SAC",
        description="Optional",
    )

    CNS: _CNS | None = Field(
        default=None,
        title="CNS",
        description="Optional",
    )

    ROL: _ROL | None = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
