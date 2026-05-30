"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RDS_O13.ORDER_DETAIL_SUPPLEMENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXR import RXR

from .RDS_O13_COMPONENT import RDS_O13_COMPONENT

_NTE = NTE
_RDS_O13_COMPONENT = RDS_O13_COMPONENT
_RXR = RXR


class RDS_O13_ORDER_DETAIL_SUPPLEMENT(HL7Model):
    """HL7 v2 RDS_O13.ORDER_DETAIL_SUPPLEMENT group.

    Attributes:
        NTE (List[NTE]): required
        RXR (List[RXR]): required
        COMPONENT (Optional[List[RDS_O13_COMPONENT]]): optional
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

    COMPONENT: Optional[List[_RDS_O13_COMPONENT]] = Field(
        default=None,
        title="COMPONENT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
