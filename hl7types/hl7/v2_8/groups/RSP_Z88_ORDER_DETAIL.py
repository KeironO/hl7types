"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_Z88.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .RSP_Z88_COMPONENT import RSP_Z88_COMPONENT

_NTE = NTE
_RSP_Z88_COMPONENT = RSP_Z88_COMPONENT
_RXO = RXO
_RXR = RXR


class RSP_Z88_ORDER_DETAIL(HL7Model):
    """HL7 v2 RSP_Z88.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): Pharmacy/Treatment Order, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        COMPONENT (Optional[RSP_Z88_COMPONENT]): optional
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

    COMPONENT: Optional[_RSP_Z88_COMPONENT] = Field(
        default=None,
        title="COMPONENT",
    )

    model_config = {"populate_by_name": True}
