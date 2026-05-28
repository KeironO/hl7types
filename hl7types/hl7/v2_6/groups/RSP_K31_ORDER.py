"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RSP_K31.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXD import RXD
from ..segments.RXR import RXR

from .RSP_K31_ENCODING import RSP_K31_ENCODING
from .RSP_K31_OBSERVATION import RSP_K31_OBSERVATION
from .RSP_K31_ORDER_DETAIL import RSP_K31_ORDER_DETAIL
from .RSP_K31_TIMING import RSP_K31_TIMING

_ORC = ORC
_RSP_K31_ENCODING = RSP_K31_ENCODING
_RSP_K31_OBSERVATION = RSP_K31_OBSERVATION
_RSP_K31_ORDER_DETAIL = RSP_K31_ORDER_DETAIL
_RSP_K31_TIMING = RSP_K31_TIMING
_RXC = RXC
_RXD = RXD
_RXR = RXR


class RSP_K31_ORDER(BaseModel):
    """HL7 v2 RSP_K31.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[RSP_K31_TIMING]]): optional
        ORDER_DETAIL (Optional[RSP_K31_ORDER_DETAIL]): optional
        ENCODING (Optional[RSP_K31_ENCODING]): optional
        RXD (RXD): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBSERVATION (List[RSP_K31_OBSERVATION]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_RSP_K31_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ORDER_DETAIL: Optional[_RSP_K31_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ENCODING: Optional[_RSP_K31_ENCODING] = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    RXD: _RXD = Field(
        default=...,
        title="RXD",
        description="Required",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    OBSERVATION: List[_RSP_K31_OBSERVATION] = Field(
        default=...,
        title="OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
