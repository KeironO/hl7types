"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RGV_O01.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .RGV_O01_ENCODING import RGV_O01_ENCODING
from .RGV_O01_GIVE import RGV_O01_GIVE
from .RGV_O01_ORDER_DETAIL import RGV_O01_ORDER_DETAIL

_ORC = ORC
_RGV_O01_ENCODING = RGV_O01_ENCODING
_RGV_O01_GIVE = RGV_O01_GIVE
_RGV_O01_ORDER_DETAIL = RGV_O01_ORDER_DETAIL


class RGV_O01_ORDER(HL7Model):
    """HL7 v2 RGV_O01.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[RGV_O01_ORDER_DETAIL]): optional
        ENCODING (Optional[RGV_O01_ENCODING]): optional
        GIVE (List[RGV_O01_GIVE]): required
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_RGV_O01_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ENCODING: Optional[_RGV_O01_ENCODING] = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    GIVE: List[_RGV_O01_GIVE] = Field(
        min_length=1,
        title="GIVE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
