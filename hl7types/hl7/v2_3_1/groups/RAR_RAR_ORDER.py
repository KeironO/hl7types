"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RAR_RAR.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
        ORC (ORC): ORC - common order segment, required
        ENCODING (Optional[RAR_RAR_ENCODING]): optional
        RXA (List[RXA]): RXA - pharmacy/treatment administration segment, required
        RXR (RXR): RXR - pharmacy/treatment route segment, required
    """

    ORC: _ORC = Field(
        title="ORC",
        description="ORC - common order segment",
    )

    ENCODING: Optional[_RAR_RAR_ENCODING] = Field(
        default=None,
        title="ENCODING",
    )

    RXA: List[_RXA] = Field(
        min_length=1,
        title="RXA",
        description="RXA - pharmacy/treatment administration segment",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="RXR - pharmacy/treatment route segment",
    )

    model_config = {"populate_by_name": True}
