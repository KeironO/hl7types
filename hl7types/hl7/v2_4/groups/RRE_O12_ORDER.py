"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RRE_O12.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .RRE_O12_ENCODING import RRE_O12_ENCODING

_ORC = ORC
_RRE_O12_ENCODING = RRE_O12_ENCODING


class RRE_O12_ORDER(BaseModel):
    """HL7 v2 RRE_O12.ORDER group.

    Attributes:
        ORC (ORC): required
        ENCODING (Optional[RRE_O12_ENCODING]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ENCODING: Optional[_RRE_O12_ENCODING] = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
