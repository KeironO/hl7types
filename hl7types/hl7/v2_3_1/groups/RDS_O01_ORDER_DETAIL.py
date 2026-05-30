"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDS_O01.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXO import RXO

from .RDS_O01_ORDER_DETAIL_SUPPLEMENT import RDS_O01_ORDER_DETAIL_SUPPLEMENT

_RDS_O01_ORDER_DETAIL_SUPPLEMENT = RDS_O01_ORDER_DETAIL_SUPPLEMENT
_RXO = RXO


class RDS_O01_ORDER_DETAIL(HL7Model):
    """HL7 v2 RDS_O01.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        ORDER_DETAIL_SUPPLEMENT (Optional[RDS_O01_ORDER_DETAIL_SUPPLEMENT]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    ORDER_DETAIL_SUPPLEMENT: Optional[_RDS_O01_ORDER_DETAIL_SUPPLEMENT] = Field(
        default=None,
        title="ORDER_DETAIL_SUPPLEMENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
