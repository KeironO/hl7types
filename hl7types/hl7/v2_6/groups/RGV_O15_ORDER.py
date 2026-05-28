"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RGV_O15.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .RGV_O15_ENCODING import RGV_O15_ENCODING
from .RGV_O15_GIVE import RGV_O15_GIVE
from .RGV_O15_ORDER_DETAIL import RGV_O15_ORDER_DETAIL
from .RGV_O15_TIMING import RGV_O15_TIMING

_ORC = ORC
_RGV_O15_ENCODING = RGV_O15_ENCODING
_RGV_O15_GIVE = RGV_O15_GIVE
_RGV_O15_ORDER_DETAIL = RGV_O15_ORDER_DETAIL
_RGV_O15_TIMING = RGV_O15_TIMING


class RGV_O15_ORDER(BaseModel):
    """HL7 v2 RGV_O15.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[RGV_O15_TIMING]]): optional
        ORDER_DETAIL (Optional[RGV_O15_ORDER_DETAIL]): optional
        ENCODING (Optional[RGV_O15_ENCODING]): optional
        GIVE (List[RGV_O15_GIVE]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_RGV_O15_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ORDER_DETAIL: _RGV_O15_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ENCODING: _RGV_O15_ENCODING | None = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    GIVE: list[_RGV_O15_GIVE] = Field(
        default=...,
        title="GIVE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
