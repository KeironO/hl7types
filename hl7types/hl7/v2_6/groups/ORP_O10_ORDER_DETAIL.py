"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORP_O10.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXO import RXO
from ..segments.RXR import RXR
from .ORP_O10_COMPONENT import ORP_O10_COMPONENT

_NTE = NTE
_ORP_O10_COMPONENT = ORP_O10_COMPONENT
_RXO = RXO
_RXR = RXR


class ORP_O10_ORDER_DETAIL(BaseModel):
    """HL7 v2 ORP_O10.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        COMPONENT (Optional[List[ORP_O10_COMPONENT]]): optional
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

    COMPONENT: list[_ORP_O10_COMPONENT] | None = Field(
        default=None,
        title="COMPONENT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
