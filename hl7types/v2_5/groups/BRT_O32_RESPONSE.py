"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: BRT_O32.RESPONSE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
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

    PID: Optional[_PID] = Field(
        default=None,
        title="PID",
        description="Optional",
    )

    ORDER: Optional[List[_BRT_O32_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
