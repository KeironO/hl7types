"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SSR_U04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SAC import SAC

_EQU = EQU
_MSH = MSH
_ROL = ROL
_SAC = SAC


class SSR_U04(BaseModel):
    """HL7 v2 SSR_U04 message.

    Attributes:
        MSH (MSH): required
        EQU (EQU): required
        SAC (List[SAC]): required
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

    SAC: List[_SAC] = Field(
        default=...,
        title="SAC",
        description="Required, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
