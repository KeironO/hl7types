"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RDE_O11.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .RDE_O11_COMPONENT import RDE_O11_COMPONENT

_NTE = NTE
_RDE_O11_COMPONENT = RDE_O11_COMPONENT
_RXO = RXO
_RXR = RXR


class RDE_O11_ORDER_DETAIL(HL7Model):
    """HL7 v2 RDE_O11.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): Pharmacy/Treatment Order, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        COMPONENT (Optional[RDE_O11_COMPONENT]): optional
    """

    RXO: _RXO = Field(
        title="RXO",
        description="Pharmacy/Treatment Order",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    COMPONENT: Optional[_RDE_O11_COMPONENT] = Field(
        default=None,
        title="COMPONENT",
    )

    model_config = {"populate_by_name": True}
