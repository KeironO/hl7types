"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RDS_O13.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RXO import RXO
from .RDS_O13_ORDER_DETAIL_SUPPLEMENT import RDS_O13_ORDER_DETAIL_SUPPLEMENT

_RDS_O13_ORDER_DETAIL_SUPPLEMENT = RDS_O13_ORDER_DETAIL_SUPPLEMENT
_RXO = RXO


class RDS_O13_ORDER_DETAIL(BaseModel):
    """HL7 v2 RDS_O13.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        ORDER_DETAIL_SUPPLEMENT (Optional[RDS_O13_ORDER_DETAIL_SUPPLEMENT]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    ORDER_DETAIL_SUPPLEMENT: _RDS_O13_ORDER_DETAIL_SUPPLEMENT | None = Field(
        default=None,
        title="ORDER_DETAIL_SUPPLEMENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
