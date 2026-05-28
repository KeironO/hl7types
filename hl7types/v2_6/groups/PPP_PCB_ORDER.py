"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PPP_PCB.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .PPP_PCB_ORDER_DETAIL import PPP_PCB_ORDER_DETAIL

_ORC = ORC
_PPP_PCB_ORDER_DETAIL = PPP_PCB_ORDER_DETAIL


class PPP_PCB_ORDER(BaseModel):
    """HL7 v2 PPP_PCB.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[PPP_PCB_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_PPP_PCB_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
