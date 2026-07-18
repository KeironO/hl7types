"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RRE_O12.ENCODING
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .RRE_O12_TIMING_ENCODED import RRE_O12_TIMING_ENCODED

_NTE = NTE
_RRE_O12_TIMING_ENCODED = RRE_O12_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RRE_O12_ENCODING(HL7Model):
    """HL7 v2 RRE_O12.ENCODING group.

    Attributes:
        RXE (RXE): Pharmacy/Treatment Encoded Order, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        TIMING_ENCODED (List[RRE_O12_TIMING_ENCODED]): required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy/Treatment Encoded Order",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    TIMING_ENCODED: List[_RRE_O12_TIMING_ENCODED] = Field(
        min_length=1,
        title="TIMING_ENCODED",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Pharmacy/Treatment Component Order",
    )

    model_config = ConfigDict(populate_by_name=True)
