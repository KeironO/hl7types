"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: INU_U05
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.INV import INV
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EQU = EQU
_INV = INV
_MSH = MSH
_SFT = SFT
_UAC = UAC


class INU_U05(BaseModel):
    """HL7 v2 INU_U05 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EQU (EQU): required
        INV (List[INV]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    EQU: _EQU = Field(
        default=...,
        title="EQU",
        description="Required",
    )

    INV: list[_INV] = Field(
        default=...,
        title="INV",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
