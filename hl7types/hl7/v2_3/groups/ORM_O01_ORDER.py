"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORM_O01.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.BLG import BLG
from ..segments.CTI import CTI
from ..segments.ORC import ORC

from .ORM_O01_ORDER_DETAIL import ORM_O01_ORDER_DETAIL

_BLG = BLG
_CTI = CTI
_ORC = ORC
_ORM_O01_ORDER_DETAIL = ORM_O01_ORDER_DETAIL


class ORM_O01_ORDER(HL7Model):
    """HL7 v2 ORM_O01.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[ORM_O01_ORDER_DETAIL]): optional
        CTI (Optional[CTI]): optional
        BLG (Optional[BLG]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_ORM_O01_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    CTI: Optional[_CTI] = Field(
        default=None,
        title="CTI",
        description="Optional",
    )

    BLG: Optional[_BLG] = Field(
        default=None,
        title="BLG",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
