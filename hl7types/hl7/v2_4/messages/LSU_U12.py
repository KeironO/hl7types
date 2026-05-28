"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: LSU_U12
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.EQP import EQP
from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL

_EQP = EQP
_EQU = EQU
_MSH = MSH
_ROL = ROL


class LSU_U12(BaseModel):
    """HL7 v2 LSU_U12 message.

    Attributes:
        MSH (MSH): required
        EQU (EQU): required
        EQP (List[EQP]): required
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

    EQP: list[_EQP] = Field(
        default=...,
        title="EQP",
        description="Required, repeating",
    )

    ROL: _ROL | None = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
