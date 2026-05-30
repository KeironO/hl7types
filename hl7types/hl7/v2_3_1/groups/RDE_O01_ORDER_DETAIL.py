"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDE_O01.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .RDE_O01_COMPONENT import RDE_O01_COMPONENT

_NTE = NTE
_RDE_O01_COMPONENT = RDE_O01_COMPONENT
_RXO = RXO
_RXR = RXR


class RDE_O01_ORDER_DETAIL(HL7Model):
    """HL7 v2 RDE_O01.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        COMPONENT (Optional[RDE_O01_COMPONENT]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    COMPONENT: Optional[_RDE_O01_COMPONENT] = Field(
        default=None,
        title="COMPONENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
