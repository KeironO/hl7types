"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RAS_O01.ORDER_DETAIL_SUPPLEMENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXR import RXR

from .RAS_O01_COMPONENTS import RAS_O01_COMPONENTS

_NTE = NTE
_RAS_O01_COMPONENTS = RAS_O01_COMPONENTS
_RXR = RXR


class RAS_O01_ORDER_DETAIL_SUPPLEMENT(HL7Model):
    """HL7 v2 RAS_O01.ORDER_DETAIL_SUPPLEMENT group.

    Attributes:
        NTE (List[NTE]): NTE - notes and comments segment, required
        RXR (List[RXR]): RXR - pharmacy/treatment route segment, required
        COMPONENTS (Optional[RAS_O01_COMPONENTS]): optional
    """

    NTE: List[_NTE] = Field(
        min_length=1,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="RXR - pharmacy/treatment route segment",
    )

    COMPONENTS: Optional[_RAS_O01_COMPONENTS] = Field(
        default=None,
        title="COMPONENTS",
    )

    model_config = {"populate_by_name": True}
