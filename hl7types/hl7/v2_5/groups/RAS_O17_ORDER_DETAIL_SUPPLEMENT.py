"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RAS_O17.ORDER_DETAIL_SUPPLEMENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXR import RXR
from .RAS_O17_COMPONENTS import RAS_O17_COMPONENTS

_NTE = NTE
_RAS_O17_COMPONENTS = RAS_O17_COMPONENTS
_RXR = RXR


class RAS_O17_ORDER_DETAIL_SUPPLEMENT(BaseModel):
    """HL7 v2 RAS_O17.ORDER_DETAIL_SUPPLEMENT group.

    Attributes:
        NTE (List[NTE]): required
        RXR (List[RXR]): required
        COMPONENTS (Optional[List[RAS_O17_COMPONENTS]]): optional
    """

    NTE: list[_NTE] = Field(
        default=...,
        title="NTE",
        description="Required, repeating",
    )

    RXR: list[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    COMPONENTS: list[_RAS_O17_COMPONENTS] | None = Field(
        default=None,
        title="COMPONENTS",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
