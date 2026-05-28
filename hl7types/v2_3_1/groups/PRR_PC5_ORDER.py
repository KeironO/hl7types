"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PRR_PC5.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .PRR_PC5_ORDER_DETAIL import PRR_PC5_ORDER_DETAIL

_ORC = ORC
_PRR_PC5_ORDER_DETAIL = PRR_PC5_ORDER_DETAIL


class PRR_PC5_ORDER(BaseModel):
    """HL7 v2 PRR_PC5.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[PRR_PC5_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_PRR_PC5_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
