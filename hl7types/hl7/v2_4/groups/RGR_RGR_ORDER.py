"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RGR_RGR.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXG import RXG
from ..segments.RXR import RXR

from .RGR_RGR_ENCODING import RGR_RGR_ENCODING

_ORC = ORC
_RGR_RGR_ENCODING = RGR_RGR_ENCODING
_RXC = RXC
_RXG = RXG
_RXR = RXR


class RGR_RGR_ORDER(BaseModel):
    """HL7 v2 RGR_RGR.ORDER group.

    Attributes:
        ORC (ORC): required
        ENCODING (Optional[RGR_RGR_ENCODING]): optional
        RXG (List[RXG]): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ENCODING: Optional[_RGR_RGR_ENCODING] = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    RXG: List[_RXG] = Field(
        default=...,
        title="RXG",
        description="Required, repeating",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
