"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RAS_O17.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RXO import RXO
from .RAS_O17_ORDER_DETAIL_SUPPLEMENT import RAS_O17_ORDER_DETAIL_SUPPLEMENT

_RAS_O17_ORDER_DETAIL_SUPPLEMENT = RAS_O17_ORDER_DETAIL_SUPPLEMENT
_RXO = RXO


class RAS_O17_ORDER_DETAIL(BaseModel):
    """HL7 v2 RAS_O17.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        ORDER_DETAIL_SUPPLEMENT (Optional[RAS_O17_ORDER_DETAIL_SUPPLEMENT]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    ORDER_DETAIL_SUPPLEMENT: _RAS_O17_ORDER_DETAIL_SUPPLEMENT | None = Field(
        default=None,
        title="ORDER_DETAIL_SUPPLEMENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
