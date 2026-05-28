"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OMS_O01.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.ORC import ORC
from .OMS_O01_ORDER_DETAIL import OMS_O01_ORDER_DETAIL

_BLG = BLG
_OMS_O01_ORDER_DETAIL = OMS_O01_ORDER_DETAIL
_ORC = ORC


class OMS_O01_ORDER(BaseModel):
    """HL7 v2 OMS_O01.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[OMS_O01_ORDER_DETAIL]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: _OMS_O01_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    BLG: _BLG | None = Field(
        default=None,
        title="BLG",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
