"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: TCU_U10
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.TCC import TCC

_EQU = EQU
_MSH = MSH
_ROL = ROL
_TCC = TCC


class TCU_U10(BaseModel):
    """HL7 v2 TCU_U10 message.

    Attributes:
        MSH (MSH): required
        EQU (EQU): required
        TCC (List[TCC]): required
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

    TCC: List[_TCC] = Field(
        default=...,
        title="TCC",
        description="Required, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
