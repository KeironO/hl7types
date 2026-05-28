"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RDE_O11.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.BLG import BLG
from ..segments.CTI import CTI
from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR
from .RDE_O11_OBSERVATION import RDE_O11_OBSERVATION
from .RDE_O11_ORDER_DETAIL import RDE_O11_ORDER_DETAIL
from .RDE_O11_TIMING import RDE_O11_TIMING
from .RDE_O11_TIMING_ENCODED import RDE_O11_TIMING_ENCODED

_BLG = BLG
_CTI = CTI
_FT1 = FT1
_NTE = NTE
_ORC = ORC
_RDE_O11_OBSERVATION = RDE_O11_OBSERVATION
_RDE_O11_ORDER_DETAIL = RDE_O11_ORDER_DETAIL
_RDE_O11_TIMING = RDE_O11_TIMING
_RDE_O11_TIMING_ENCODED = RDE_O11_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RDE_O11_ORDER(BaseModel):
    """HL7 v2 RDE_O11.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[RDE_O11_TIMING]]): optional
        ORDER_DETAIL (Optional[RDE_O11_ORDER_DETAIL]): optional
        RXE (RXE): required
        NTE (Optional[List[NTE]]): optional
        TIMING_ENCODED (List[RDE_O11_TIMING_ENCODED]): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBSERVATION (Optional[List[RDE_O11_OBSERVATION]]): optional
        FT1 (Optional[List[FT1]]): optional
        BLG (Optional[BLG]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_RDE_O11_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ORDER_DETAIL: _RDE_O11_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_ENCODED: list[_RDE_O11_TIMING_ENCODED] = Field(
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

    OBSERVATION: list[_RDE_O11_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    FT1: list[_FT1] | None = Field(
        default=None,
        title="FT1",
        description="Optional, repeating",
    )

    BLG: _BLG | None = Field(
        default=None,
        title="BLG",
        description="Optional",
    )

    CTI: list[_CTI] | None = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
