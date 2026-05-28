"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_Z88.COMMON_ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXD import RXD
from ..segments.RXR import RXR
from .RSP_Z88_OBSERVATION import RSP_Z88_OBSERVATION
from .RSP_Z88_ORDER_DETAIL import RSP_Z88_ORDER_DETAIL
from .RSP_Z88_ORDER_ENCODED import RSP_Z88_ORDER_ENCODED
from .RSP_Z88_TIMING import RSP_Z88_TIMING

_ORC = ORC
_RSP_Z88_OBSERVATION = RSP_Z88_OBSERVATION
_RSP_Z88_ORDER_DETAIL = RSP_Z88_ORDER_DETAIL
_RSP_Z88_ORDER_ENCODED = RSP_Z88_ORDER_ENCODED
_RSP_Z88_TIMING = RSP_Z88_TIMING
_RXC = RXC
_RXD = RXD
_RXR = RXR


class RSP_Z88_COMMON_ORDER(BaseModel):
    """HL7 v2 RSP_Z88.COMMON_ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[RSP_Z88_TIMING]]): optional
        ORDER_DETAIL (Optional[RSP_Z88_ORDER_DETAIL]): optional
        ORDER_ENCODED (Optional[RSP_Z88_ORDER_ENCODED]): optional
        RXD (RXD): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBSERVATION (List[RSP_Z88_OBSERVATION]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: list[_RSP_Z88_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ORDER_DETAIL: _RSP_Z88_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ORDER_ENCODED: _RSP_Z88_ORDER_ENCODED | None = Field(
        default=None,
        title="ORDER_ENCODED",
        description="Optional",
    )

    RXD: _RXD = Field(
        default=...,
        title="RXD",
        description="Required",
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

    OBSERVATION: list[_RSP_Z88_OBSERVATION] = Field(
        default=...,
        title="OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
