"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PGL_PC6.ORDER
Type: Group
"""

from __future__ import annotations

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

    ORDER_DETAIL: _PGL_PC6_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
