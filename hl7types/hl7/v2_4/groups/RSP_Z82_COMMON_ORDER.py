"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z82.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXD import RXD
from ..segments.RXR import RXR

from .RSP_Z82_ENCODED_ORDER import RSP_Z82_ENCODED_ORDER
from .RSP_Z82_OBSERVATION import RSP_Z82_OBSERVATION
from .RSP_Z82_ORDER_DETAIL import RSP_Z82_ORDER_DETAIL

_ORC = ORC
_RSP_Z82_ENCODED_ORDER = RSP_Z82_ENCODED_ORDER
_RSP_Z82_OBSERVATION = RSP_Z82_OBSERVATION
_RSP_Z82_ORDER_DETAIL = RSP_Z82_ORDER_DETAIL
_RXC = RXC
_RXD = RXD
_RXR = RXR


class RSP_Z82_COMMON_ORDER(BaseModel):
    """HL7 v2 RSP_Z82.COMMON_ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[RSP_Z82_ORDER_DETAIL]): optional
        ENCODED_ORDER (Optional[RSP_Z82_ENCODED_ORDER]): optional
        RXD (RXD): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBSERVATION (List[RSP_Z82_OBSERVATION]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_RSP_Z82_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ENCODED_ORDER: Optional[_RSP_Z82_ENCODED_ORDER] = Field(
        default=None,
        title="ENCODED_ORDER",
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

    OBSERVATION: List[_RSP_Z82_OBSERVATION] = Field(
        default=...,
        title="OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
