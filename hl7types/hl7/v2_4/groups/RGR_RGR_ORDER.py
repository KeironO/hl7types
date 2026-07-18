"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RGR_RGR.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        ORC (ORC): Common Order, required
        ENCODING (Optional[RGR_RGR_ENCODING]): optional
        RXG (List[RXG]): Pharmacy/Treatment Give, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    ENCODING: Optional[_RGR_RGR_ENCODING] = Field(
        default=None,
        title="ENCODING",
    )

    RXG: List[_RXG] = Field(
        min_length=1,
        title="RXG",
        description="Pharmacy/Treatment Give",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Pharmacy/Treatment Component Order",
    )

    model_config = ConfigDict(populate_by_name=True)
