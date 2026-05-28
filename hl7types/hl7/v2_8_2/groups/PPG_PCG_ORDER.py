"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PPG_PCG.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .PPG_PCG_ORDER_DETAIL import PPG_PCG_ORDER_DETAIL

_ORC = ORC
_PPG_PCG_ORDER_DETAIL = PPG_PCG_ORDER_DETAIL


class PPG_PCG_ORDER(BaseModel):
    """HL7 v2 PPG_PCG.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[PPG_PCG_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: _PPG_PCG_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
