"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDO_O01.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.ORC import ORC
from .RDO_O01_ORDER_DETAIL import RDO_O01_ORDER_DETAIL

_BLG = BLG
_ORC = ORC
_RDO_O01_ORDER_DETAIL = RDO_O01_ORDER_DETAIL


class RDO_O01_ORDER(BaseModel):
    """HL7 v2 RDO_O01.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[RDO_O01_ORDER_DETAIL]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: _RDO_O01_ORDER_DETAIL | None = Field(
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
