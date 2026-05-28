"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RGV_O01.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .RGV_O01_ENCODING import RGV_O01_ENCODING
from .RGV_O01_GIVE import RGV_O01_GIVE
from .RGV_O01_ORDER_DETAIL import RGV_O01_ORDER_DETAIL

_ORC = ORC
_RGV_O01_ENCODING = RGV_O01_ENCODING
_RGV_O01_GIVE = RGV_O01_GIVE
_RGV_O01_ORDER_DETAIL = RGV_O01_ORDER_DETAIL


class RGV_O01_ORDER(BaseModel):
    """HL7 v2 RGV_O01.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[RGV_O01_ORDER_DETAIL]): optional
        ENCODING (Optional[RGV_O01_ENCODING]): optional
        GIVE (List[RGV_O01_GIVE]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: _RGV_O01_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ENCODING: _RGV_O01_ENCODING | None = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    GIVE: list[_RGV_O01_GIVE] = Field(
        default=...,
        title="GIVE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
