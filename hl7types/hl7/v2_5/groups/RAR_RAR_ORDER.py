"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RAR_RAR.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .RAR_RAR_ENCODING import RAR_RAR_ENCODING

_ORC = ORC
_RAR_RAR_ENCODING = RAR_RAR_ENCODING
_RXA = RXA
_RXR = RXR


class RAR_RAR_ORDER(HL7Model):
    """HL7 v2 RAR_RAR.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        ENCODING (Optional[RAR_RAR_ENCODING]): optional
        RXA (List[RXA]): Pharmacy/Treatment Administration, required
        RXR (RXR): Pharmacy/Treatment Route, required
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    ENCODING: Optional[_RAR_RAR_ENCODING] = Field(
        default=None,
        title="ENCODING",
    )

    RXA: List[_RXA] = Field(
        min_length=1,
        title="RXA",
        description="Pharmacy/Treatment Administration",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    model_config = ConfigDict(populate_by_name=True)
