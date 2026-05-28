"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: INU_U05
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.INV import INV
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT

_EQU = EQU
_INV = INV
_MSH = MSH
_ROL = ROL
_SFT = SFT


class INU_U05(BaseModel):
    """HL7 v2 INU_U05 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EQU (EQU): required
        INV (List[INV]): required
        ROL (Optional[ROL]): optional
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

    ROL: _ROL | None = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
