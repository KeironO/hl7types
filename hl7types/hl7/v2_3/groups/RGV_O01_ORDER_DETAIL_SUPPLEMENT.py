"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RGV_O01.ORDER_DETAIL_SUPPLEMENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXR import RXR

from .RGV_O01_COMPONENTS import RGV_O01_COMPONENTS

_NTE = NTE
_RGV_O01_COMPONENTS = RGV_O01_COMPONENTS
_RXR = RXR


class RGV_O01_ORDER_DETAIL_SUPPLEMENT(HL7Model):
    """HL7 v2 RGV_O01.ORDER_DETAIL_SUPPLEMENT group.

    Attributes:
        NTE (List[NTE]): required
        RXR (List[RXR]): required
        COMPONENTS (Optional[RGV_O01_COMPONENTS]): optional
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

    COMPONENTS: Optional[_RGV_O01_COMPONENTS] = Field(
        default=None,
        title="COMPONENTS",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
