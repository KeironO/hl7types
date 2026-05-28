"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RAS_O01.COMPONENTS
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXC import RXC

_NTE = NTE
_RXC = RXC


class RAS_O01_COMPONENTS(BaseModel):
    """HL7 v2 RAS_O01.COMPONENTS group.

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
