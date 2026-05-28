"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RAS_O01.ENCODING
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

_RXC = RXC
_RXE = RXE
_RXR = RXR


class RAS_O01_ENCODING(BaseModel):
    """HL7 v2 RAS_O01.ENCODING group.

    Attributes:
        RXE (RXE): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXE: _RXE = Field(
        default=...,
        title="RXE",
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
