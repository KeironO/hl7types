"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RDE_O11.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class RDE_O11_ORDER_DETAIL(HL7Model):
    """HL7 v2 RDE_O11.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): Pharmacy/Treatment Order, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        COMPONENTS (Optional[List[RDE_O11_COMPONENTS]]): optional
    """

    RXO: _RXO = Field(
        title="RXO",
        description="Pharmacy/Treatment Order",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
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

    COMPONENTS: Optional[List[_RDE_O11_COMPONENTS]] = Field(
        default=None,
        title="COMPONENTS",
    )

    model_config = {"populate_by_name": True}
