"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RAS_O17.ENCODING
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CDO import CDO
from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR
from .RAS_O17_TIMING_ENCODED import RAS_O17_TIMING_ENCODED

_CDO = CDO
_NTE = NTE
_PRT = PRT
_RAS_O17_TIMING_ENCODED = RAS_O17_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RAS_O17_ENCODING(BaseModel):
    """HL7 v2 RAS_O17.ENCODING group.

    Attributes:
        RXE (RXE): required
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        TIMING_ENCODED (List[RAS_O17_TIMING_ENCODED]): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        CDO (Optional[List[CDO]]): optional
    """

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_ENCODED: list[_RAS_O17_TIMING_ENCODED] = Field(
        default=...,
        title="TIMING_ENCODED",
        description="Required, repeating",
    )

    RXR: list[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: list[_RXC] | None = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    CDO: list[_CDO] | None = Field(
        default=None,
        title="CDO",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
