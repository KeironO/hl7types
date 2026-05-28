"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ESU_U01
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.ISD import ISD
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT

_EQU = EQU
_ISD = ISD
_MSH = MSH
_ROL = ROL
_SFT = SFT


class ESU_U01(BaseModel):
    """HL7 v2 ESU_U01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EQU (EQU): required
        ISD (Optional[List[ISD]]): optional
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

    ISD: Optional[List[_ISD]] = Field(
        default=None,
        title="ISD",
        description="Optional, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
