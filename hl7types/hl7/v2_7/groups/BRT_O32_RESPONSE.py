"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: BRT_O32.RESPONSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PID import PID
from .BRT_O32_ORDER import BRT_O32_ORDER

_BRT_O32_ORDER = BRT_O32_ORDER
_PID = PID


class BRT_O32_RESPONSE(BaseModel):
    """HL7 v2 BRT_O32.RESPONSE group.

    Attributes:
        PID (Optional[PID]): optional
        ORDER (Optional[List[BRT_O32_ORDER]]): optional
    """

    PID: _PID | None = Field(
        default=None,
        title="PID",
        description="Optional",
    )

    ORDER: list[_BRT_O32_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
