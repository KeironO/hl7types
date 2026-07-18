"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RDE_O01.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        RXO (RXO): Pharmacy prescription order segment, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        RXR (List[RXR]): Pharmacy route segment, required
        COMPONENT (Optional[RDE_O01_COMPONENT]): optional
    """

    RXO: _RXO = Field(
        title="RXO",
        description="Pharmacy prescription order segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy route segment",
    )

    COMPONENT: Optional[_RDE_O01_COMPONENT] = Field(
        default=None,
        title="COMPONENT",
    )

    model_config = ConfigDict(populate_by_name=True)
