"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RDS_O13.ENCODING
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .RDS_O13_TIMING_ENCODED import RDS_O13_TIMING_ENCODED

_NTE = NTE
_PRT = PRT
_RDS_O13_TIMING_ENCODED = RDS_O13_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RDS_O13_ENCODING(HL7Model):
    """HL7 v2 RDS_O13.ENCODING group.

    Attributes:
        RXE (RXE): required
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        TIMING_ENCODED (List[RDS_O13_TIMING_ENCODED]): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_ENCODED: List[_RDS_O13_TIMING_ENCODED] = Field(
        min_length=1,
        title="TIMING_ENCODED",
        description="Required, repeating",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
