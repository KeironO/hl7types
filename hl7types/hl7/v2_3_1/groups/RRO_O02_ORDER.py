"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRO_O02.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .RRO_O02_ORDER_DETAIL import RRO_O02_ORDER_DETAIL

_ORC = ORC
_RRO_O02_ORDER_DETAIL = RRO_O02_ORDER_DETAIL


class RRO_O02_ORDER(BaseModel):
    """HL7 v2 RRO_O02.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[RRO_O02_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_RRO_O02_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
