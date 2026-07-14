"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RGR_RGR.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class RGR_RGR_ORDER(HL7Model):
    """HL7 v2 RGR_RGR.ORDER group.

    Attributes:
        ORC (ORC): ORC - common order segment, required
        ENCODING (Optional[RGR_RGR_ENCODING]): optional
        RXG (List[RXG]): RXG - pharmacy/treatment give segment, required
        RXR (List[RXR]): RXR - pharmacy/treatment route segment, required
        RXC (Optional[List[RXC]]): RXC - pharmacy/treatment component order segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="ORC - common order segment",
    )

    ENCODING: Optional[_RGR_RGR_ENCODING] = Field(
        default=None,
        title="ENCODING",
    )

    RXG: List[_RXG] = Field(
        min_length=1,
        title="RXG",
        description="RXG - pharmacy/treatment give segment",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="RXR - pharmacy/treatment route segment",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="RXC - pharmacy/treatment component order segment",
    )

    model_config = {"populate_by_name": True}
