"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OMN_O01.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.ORC import ORC

from .OMN_O01_ORDER_DETAIL import OMN_O01_ORDER_DETAIL

_BLG = BLG
_OMN_O01_ORDER_DETAIL = OMN_O01_ORDER_DETAIL
_ORC = ORC


class OMN_O01_ORDER(BaseModel):
    """HL7 v2 OMN_O01.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[OMN_O01_ORDER_DETAIL]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_OMN_O01_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    BLG: Optional[_BLG] = Field(
        default=None,
        title="BLG",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
