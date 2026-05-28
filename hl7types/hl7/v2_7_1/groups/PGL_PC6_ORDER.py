"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PGL_PC6.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .PGL_PC6_ORDER_DETAIL import PGL_PC6_ORDER_DETAIL

_ORC = ORC
_PGL_PC6_ORDER_DETAIL = PGL_PC6_ORDER_DETAIL


class PGL_PC6_ORDER(BaseModel):
    """HL7 v2 PGL_PC6.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[PGL_PC6_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_PGL_PC6_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
