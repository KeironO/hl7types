"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RAR_RAR.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.RXA import RXA
from ..segments.RXR import RXR
from .RAR_RAR_ENCODING import RAR_RAR_ENCODING

_ORC = ORC
_RAR_RAR_ENCODING = RAR_RAR_ENCODING
_RXA = RXA
_RXR = RXR


class RAR_RAR_ORDER(BaseModel):
    """HL7 v2 RAR_RAR.ORDER group.

    Attributes:
        ORC (ORC): required
        ENCODING (Optional[RAR_RAR_ENCODING]): optional
        RXA (List[RXA]): required
        RXR (RXR): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ENCODING: _RAR_RAR_ENCODING | None = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    RXA: list[_RXA] = Field(
        default=...,
        title="RXA",
        description="Required, repeating",
    )

    RXR: _RXR = Field(
        default=...,
        title="RXR",
        description="Required",
    )

    model_config = {"populate_by_name": True}
