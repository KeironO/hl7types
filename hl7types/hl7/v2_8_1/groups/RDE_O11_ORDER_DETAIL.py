"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
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

from .RDE_O11_COMPONENT import RDE_O11_COMPONENT

_NTE = NTE
_PRT = PRT
_RDE_O11_COMPONENT = RDE_O11_COMPONENT
_RXO = RXO
_RXR = RXR


class RDE_O11_ORDER_DETAIL(HL7Model):
    """HL7 v2 RDE_O11.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        COMPONENT (Optional[List[RDE_O11_COMPONENT]]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
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

    COMPONENT: Optional[List[_RDE_O11_COMPONENT]] = Field(
        default=None,
        title="COMPONENT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
