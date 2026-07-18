"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RSP_Z82.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXO import RXO
from ..segments.RXR import RXR

from .RSP_Z82_TREATMENT import RSP_Z82_TREATMENT

_NTE = NTE
_RSP_Z82_TREATMENT = RSP_Z82_TREATMENT
_RXO = RXO
_RXR = RXR


class RSP_Z82_ORDER_DETAIL(HL7Model):
    """HL7 v2 RSP_Z82.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): Pharmacy/Treatment Order, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        TREATMENT (Optional[RSP_Z82_TREATMENT]): optional
    """

    RXO: _RXO = Field(
        title="RXO",
        description="Pharmacy/Treatment Order",
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

    TREATMENT: Optional[_RSP_Z82_TREATMENT] = Field(
        default=None,
        title="TREATMENT",
    )

    model_config = ConfigDict(populate_by_name=True)
