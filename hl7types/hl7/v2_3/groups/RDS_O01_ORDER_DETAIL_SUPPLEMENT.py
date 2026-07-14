"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RDS_O01.ORDER_DETAIL_SUPPLEMENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXR import RXR

from .RDS_O01_COMPONENT import RDS_O01_COMPONENT

_NTE = NTE
_RDS_O01_COMPONENT = RDS_O01_COMPONENT
_RXR = RXR


class RDS_O01_ORDER_DETAIL_SUPPLEMENT(HL7Model):
    """HL7 v2 RDS_O01.ORDER_DETAIL_SUPPLEMENT group.

    Attributes:
        NTE (List[NTE]): Notes and comments segment, required
        RXR (List[RXR]): Pharmacy route segment, required
        COMPONENT (Optional[RDS_O01_COMPONENT]): optional
    """

    NTE: List[_NTE] = Field(
        min_length=1,
        title="NTE",
        description="Notes and comments segment",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy route segment",
    )

    COMPONENT: Optional[_RDS_O01_COMPONENT] = Field(
        default=None,
        title="COMPONENT",
    )

    model_config = {"populate_by_name": True}
