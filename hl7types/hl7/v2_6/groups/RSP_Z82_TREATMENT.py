"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RSP_Z82.TREATMENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXC import RXC

_NTE = NTE
_RXC = RXC


class RSP_Z82_TREATMENT(HL7Model):
    """HL7 v2 RSP_Z82.TREATMENT group.

    Attributes:
        RXC (List[RXC]): Pharmacy/Treatment Component Order, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    RXC: List[_RXC] = Field(
        min_length=1,
        title="RXC",
        description="Pharmacy/Treatment Component Order",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)
