"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OMS_O01.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.BLG import BLG
from ..segments.ORC import ORC

from .OMS_O01_ORDER_DETAIL import OMS_O01_ORDER_DETAIL

_BLG = BLG
_OMS_O01_ORDER_DETAIL = OMS_O01_ORDER_DETAIL
_ORC = ORC


class OMS_O01_ORDER(HL7Model):
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

    ORDER_DETAIL: Optional[_OMS_O01_ORDER_DETAIL] = Field(
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
