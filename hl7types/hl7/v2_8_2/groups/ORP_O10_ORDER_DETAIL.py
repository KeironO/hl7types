"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORP_O10.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .ORP_O10_COMPONENT import ORP_O10_COMPONENT

_NTE = NTE
_ORP_O10_COMPONENT = ORP_O10_COMPONENT
_PRT = PRT
_RXO = RXO
_RXR = RXR


class ORP_O10_ORDER_DETAIL(HL7Model):
    """HL7 v2 ORP_O10.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): Pharmacy/Treatment Order, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        COMPONENT (Optional[List[ORP_O10_COMPONENT]]): optional
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

    COMPONENT: Optional[List[_ORP_O10_COMPONENT]] = Field(
        default=None,
        title="COMPONENT",
    )

    model_config = ConfigDict(populate_by_name=True)
