"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RDE_O11.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

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


class RDE_O11_ORDER(BaseModel):
    """HL7 v2 RDE_O11.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[RDE_O11_ORDER_DETAIL]): optional
        RXE (RXE): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBSERVATION (Optional[List[RDE_O11_OBSERVATION]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_RDE_O11_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    RXE: _RXE = Field(
        default=...,
        title="RXE",
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

    OBSERVATION: Optional[List[_RDE_O11_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
