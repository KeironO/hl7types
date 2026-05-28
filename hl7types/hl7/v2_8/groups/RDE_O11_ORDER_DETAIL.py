"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RDE_O11.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.RXO import RXO
from ..segments.RXR import RXR
from .RDE_O11_COMPONENTS import RDE_O11_COMPONENTS

_NTE = NTE
_PRT = PRT
_RDE_O11_COMPONENTS = RDE_O11_COMPONENTS
_RXO = RXO
_RXR = RXR


class RDE_O11_ORDER_DETAIL(BaseModel):
    """HL7 v2 RDE_O11.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        COMPONENTS (Optional[List[RDE_O11_COMPONENTS]]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
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

    COMPONENTS: list[_RDE_O11_COMPONENTS] | None = Field(
        default=None,
        title="COMPONENTS",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
