"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RGV_O15.ORDER_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PRT import PRT
from ..segments.RXO import RXO

from .RGV_O15_ORDER_DETAIL_SUPPLEMENT import RGV_O15_ORDER_DETAIL_SUPPLEMENT

_PRT = PRT
_RGV_O15_ORDER_DETAIL_SUPPLEMENT = RGV_O15_ORDER_DETAIL_SUPPLEMENT
_RXO = RXO


class RGV_O15_ORDER_DETAIL(BaseModel):
    """HL7 v2 RGV_O15.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        PRT (Optional[List[PRT]]): optional
        ORDER_DETAIL_SUPPLEMENT (Optional[RGV_O15_ORDER_DETAIL_SUPPLEMENT]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ORDER_DETAIL_SUPPLEMENT: Optional[_RGV_O15_ORDER_DETAIL_SUPPLEMENT] = Field(
        default=None,
        title="ORDER_DETAIL_SUPPLEMENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
