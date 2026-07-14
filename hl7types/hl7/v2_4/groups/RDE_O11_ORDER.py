"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RDE_O11.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .RDE_O11_OBSERVATION import RDE_O11_OBSERVATION
from .RDE_O11_ORDER_DETAIL import RDE_O11_ORDER_DETAIL

_CTI = CTI
_ORC = ORC
_RDE_O11_OBSERVATION = RDE_O11_OBSERVATION
_RDE_O11_ORDER_DETAIL = RDE_O11_ORDER_DETAIL
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RDE_O11_ORDER(HL7Model):
    """HL7 v2 RDE_O11.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        ORDER_DETAIL (Optional[RDE_O11_ORDER_DETAIL]): optional
        RXE (RXE): Pharmacy/Treatment Encoded Order, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
        OBSERVATION (Optional[List[RDE_O11_OBSERVATION]]): optional
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    ORDER_DETAIL: Optional[_RDE_O11_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
    )

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy/Treatment Encoded Order",
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

    OBSERVATION: Optional[List[_RDE_O11_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    model_config = {"populate_by_name": True}
