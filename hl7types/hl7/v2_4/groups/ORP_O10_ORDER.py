"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORP_O10.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .ORP_O10_ORDER_DETAIL import ORP_O10_ORDER_DETAIL

_ORC = ORC
_ORP_O10_ORDER_DETAIL = ORP_O10_ORDER_DETAIL


class ORP_O10_ORDER(BaseModel):
    """HL7 v2 ORP_O10.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[ORP_O10_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_ORP_O10_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
