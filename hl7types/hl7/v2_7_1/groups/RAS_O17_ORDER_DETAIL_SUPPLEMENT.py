"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RAS_O17.ORDER_DETAIL_SUPPLEMENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        NTE (List[NTE]): Notes and Comments, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        COMPONENTS (Optional[List[RAS_O17_COMPONENTS]]): optional
    """

    NTE: List[_NTE] = Field(
        min_length=1,
        title="NTE",
        description="Notes and Comments",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    COMPONENTS: Optional[List[_RAS_O17_COMPONENTS]] = Field(
        default=None,
        title="COMPONENTS",
    )

    model_config = ConfigDict(populate_by_name=True)
