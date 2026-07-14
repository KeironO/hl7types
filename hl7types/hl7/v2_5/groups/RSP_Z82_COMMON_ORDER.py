"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RSP_Z82.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXD import RXD
from ..segments.RXR import RXR

from .RSP_Z82_ENCODED_ORDER import RSP_Z82_ENCODED_ORDER
from .RSP_Z82_OBSERVATION import RSP_Z82_OBSERVATION
from .RSP_Z82_ORDER_DETAIL import RSP_Z82_ORDER_DETAIL
from .RSP_Z82_TIMING import RSP_Z82_TIMING

_ORC = ORC
_RSP_Z82_ENCODED_ORDER = RSP_Z82_ENCODED_ORDER
_RSP_Z82_OBSERVATION = RSP_Z82_OBSERVATION
_RSP_Z82_ORDER_DETAIL = RSP_Z82_ORDER_DETAIL
_RSP_Z82_TIMING = RSP_Z82_TIMING
_RXC = RXC
_RXD = RXD
_RXR = RXR


class RSP_Z82_COMMON_ORDER(HL7Model):
    """HL7 v2 RSP_Z82.COMMON_ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[RSP_Z82_TIMING]]): optional
        ORDER_DETAIL (Optional[RSP_Z82_ORDER_DETAIL]): optional
        ENCODED_ORDER (Optional[RSP_Z82_ENCODED_ORDER]): optional
        RXD (RXD): Pharmacy/Treatment Dispense, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
        OBSERVATION (List[RSP_Z82_OBSERVATION]): required
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_RSP_Z82_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    ORDER_DETAIL: Optional[_RSP_Z82_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
    )

    ENCODED_ORDER: Optional[_RSP_Z82_ENCODED_ORDER] = Field(
        default=None,
        title="ENCODED_ORDER",
    )

    RXD: _RXD = Field(
        title="RXD",
        description="Pharmacy/Treatment Dispense",
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

    OBSERVATION: List[_RSP_Z82_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = {"populate_by_name": True}
