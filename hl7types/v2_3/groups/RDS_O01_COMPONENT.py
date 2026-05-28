"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RDS_O01.COMPONENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXC import RXC

_NTE = NTE
_RXC = RXC


class RDS_O01_COMPONENT(BaseModel):
    """HL7 v2 RDS_O01.COMPONENT group.

    Attributes:
        RXC (List[RXC]): required
        NTE (Optional[List[NTE]]): optional
    """

    RXC: List[_RXC] = Field(
        default=...,
        title="RXC",
        description="Required, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
