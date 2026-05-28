"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORM_O01.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.CTI import CTI
from ..segments.FT1 import FT1
from ..segments.ORC import ORC
from .ORM_O01_ORDER_DETAIL import ORM_O01_ORDER_DETAIL

_BLG = BLG
_CTI = CTI
_FT1 = FT1
_ORC = ORC
_ORM_O01_ORDER_DETAIL = ORM_O01_ORDER_DETAIL


class ORM_O01_ORDER(BaseModel):
    """HL7 v2 ORM_O01.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[ORM_O01_ORDER_DETAIL]): optional
        FT1 (Optional[List[FT1]]): optional
        CTI (Optional[List[CTI]]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: _ORM_O01_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    FT1: list[_FT1] | None = Field(
        default=None,
        title="FT1",
        description="Optional, repeating",
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    BLG: _BLG | None = Field(
        default=None,
        title="BLG",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
