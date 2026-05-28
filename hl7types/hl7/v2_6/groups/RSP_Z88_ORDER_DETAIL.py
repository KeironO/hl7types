"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RSP_Z88.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXO import RXO
from ..segments.RXR import RXR
from .RSP_Z88_COMPONENT import RSP_Z88_COMPONENT

_NTE = NTE
_RSP_Z88_COMPONENT = RSP_Z88_COMPONENT
_RXO = RXO
_RXR = RXR


class RSP_Z88_ORDER_DETAIL(BaseModel):
    """HL7 v2 RSP_Z88.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        COMPONENT (Optional[RSP_Z88_COMPONENT]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RXR: list[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    COMPONENT: _RSP_Z88_COMPONENT | None = Field(
        default=None,
        title="COMPONENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
