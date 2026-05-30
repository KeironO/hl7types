"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: LSU_U12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQP import EQP
from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT

_EQP = EQP
_EQU = EQU
_MSH = MSH
_ROL = ROL
_SFT = SFT


class LSU_U12(HL7Model):
    """HL7 v2 LSU_U12 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EQU (EQU): required
        EQP (List[EQP]): required
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

    EQP: List[_EQP] = Field(
        default=...,
        title="EQP",
        description="Required, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
