"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RAS_O17.ORDER_DETAIL_SUPPLEMENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXR import RXR

from .RAS_O17_COMPONENTS import RAS_O17_COMPONENTS

_NTE = NTE
_RAS_O17_COMPONENTS = RAS_O17_COMPONENTS
_RXR = RXR


class RAS_O17_ORDER_DETAIL_SUPPLEMENT(HL7Model):
    """HL7 v2 RAS_O17.ORDER_DETAIL_SUPPLEMENT group.

    Attributes:
        NTE (List[NTE]): required
        RXR (List[RXR]): required
        COMPONENTS (Optional[List[RAS_O17_COMPONENTS]]): optional
    """

    NTE: List[_NTE] = Field(
        default=...,
        title="NTE",
        description="Required, repeating",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    COMPONENTS: Optional[List[_RAS_O17_COMPONENTS]] = Field(
        default=None,
        title="COMPONENTS",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
