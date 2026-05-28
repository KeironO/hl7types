"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PPT_PCL.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .PPT_PCL_ORDER_DETAIL import PPT_PCL_ORDER_DETAIL

_ORC = ORC
_PPT_PCL_ORDER_DETAIL = PPT_PCL_ORDER_DETAIL


class PPT_PCL_ORDER(BaseModel):
    """HL7 v2 PPT_PCL.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[PPT_PCL_ORDER_DETAIL]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_PPT_PCL_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
