"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RDE_O01.ORDER
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

from .RDE_O01_OBSERVATION import RDE_O01_OBSERVATION
from .RDE_O01_ORDER_DETAIL import RDE_O01_ORDER_DETAIL

_CTI = CTI
_ORC = ORC
_RDE_O01_OBSERVATION = RDE_O01_OBSERVATION
_RDE_O01_ORDER_DETAIL = RDE_O01_ORDER_DETAIL
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RDE_O01_ORDER(HL7Model):
    """HL7 v2 RDE_O01.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[RDE_O01_ORDER_DETAIL]): optional
        RXE (RXE): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBSERVATION (List[RDE_O01_OBSERVATION]): required
        CTI (Optional[CTI]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_RDE_O01_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    RXE: _RXE = Field(
        title="RXE",
        description="Required",
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

    OBSERVATION: List[_RDE_O01_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
        description="Required, repeating",
    )

    CTI: Optional[_CTI] = Field(
        default=None,
        title="CTI",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
