"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RAR_RAR.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.RXA import RXA

from .RAR_RAR_ENCODING import RAR_RAR_ENCODING

_ORC = ORC
_RAR_RAR_ENCODING = RAR_RAR_ENCODING
_RXA = RXA


class RAR_RAR_ORDER(HL7Model):
    """HL7 v2 RAR_RAR.ORDER group.

    Attributes:
        ORC (ORC): required
        ENCODING (Optional[RAR_RAR_ENCODING]): optional
        RXA (List[RXA]): required
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    ENCODING: Optional[_RAR_RAR_ENCODING] = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    RXA: List[_RXA] = Field(
        min_length=1,
        title="RXA",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
