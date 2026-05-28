"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RSP_K31.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXO import RXO
from ..segments.RXR import RXR
from .RSP_K31_COMPONENTS import RSP_K31_COMPONENTS

_NTE = NTE
_RSP_K31_COMPONENTS = RSP_K31_COMPONENTS
_RXO = RXO
_RXR = RXR


class RSP_K31_ORDER_DETAIL(BaseModel):
    """HL7 v2 RSP_K31.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        COMPONENTS (Optional[List[RSP_K31_COMPONENTS]]): optional
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

    COMPONENTS: list[_RSP_K31_COMPONENTS] | None = Field(
        default=None,
        title="COMPONENTS",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
