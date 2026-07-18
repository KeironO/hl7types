"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RSP_K31.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class RSP_K31_ORDER(HL7Model):
    """HL7 v2 RSP_K31.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[RSP_K31_TIMING]]): optional
        ORDER_DETAIL (Optional[RSP_K31_ORDER_DETAIL]): optional
        ENCODING (Optional[RSP_K31_ENCODING]): optional
        RXD (RXD): Pharmacy/Treatment Dispense, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
        OBSERVATION (List[RSP_K31_OBSERVATION]): required
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_RSP_K31_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    ORDER_DETAIL: Optional[_RSP_K31_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
    )

    ENCODING: Optional[_RSP_K31_ENCODING] = Field(
        default=None,
        title="ENCODING",
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

    OBSERVATION: List[_RSP_K31_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
