"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PPR_PC1.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .PPR_PC1_ORDER_DETAIL import PPR_PC1_ORDER_DETAIL

_ORC = ORC
_PPR_PC1_ORDER_DETAIL = PPR_PC1_ORDER_DETAIL


class PPR_PC1_ORDER(BaseModel):
    """HL7 v2 PPR_PC1.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[PPR_PC1_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: _PPR_PC1_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
