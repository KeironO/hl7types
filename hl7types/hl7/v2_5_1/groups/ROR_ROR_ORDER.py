"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ROR_ROR.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

_ORC = ORC
_RXC = RXC
_RXO = RXO
_RXR = RXR


class ROR_ROR_ORDER(BaseModel):
    """HL7 v2 ROR_ROR.ORDER group.

    Attributes:
        ORC (ORC): required
        RXO (RXO): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    RXR: list[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: list[_RXC] | None = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
