"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORM_O01.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.CTI import CTI
from ..segments.ORC import ORC
from .ORM_O01_ORDER_DETAIL import ORM_O01_ORDER_DETAIL

_BLG = BLG
_CTI = CTI
_ORC = ORC
_ORM_O01_ORDER_DETAIL = ORM_O01_ORDER_DETAIL


class ORM_O01_ORDER(BaseModel):
    """HL7 v2 ORM_O01.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[ORM_O01_ORDER_DETAIL]): optional
        CTI (Optional[CTI]): optional
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

    CTI: _CTI | None = Field(
        default=None,
        title="CTI",
        description="Optional",
    )

    BLG: _BLG | None = Field(
        default=None,
        title="BLG",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
