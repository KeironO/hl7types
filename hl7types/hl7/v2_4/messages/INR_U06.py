"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: INR_U06
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.INV import INV
from ..segments.MSH import MSH
from ..segments.ROL import ROL

_EQU = EQU
_INV = INV
_MSH = MSH
_ROL = ROL


class INR_U06(BaseModel):
    """HL7 v2 INR_U06 message.

    Attributes:
        MSH (MSH): required
        EQU (EQU): required
        INV (List[INV]): required
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

    INV: List[_INV] = Field(
        default=...,
        title="INV",
        description="Required, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
