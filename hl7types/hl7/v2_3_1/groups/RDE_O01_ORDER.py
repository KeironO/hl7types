"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDE_O01.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
        ORC (ORC): ORC - common order segment, required
        ORDER_DETAIL (Optional[RDE_O01_ORDER_DETAIL]): optional
        RXE (RXE): RXE - pharmacy/treatment encoded order segment, required
        RXR (List[RXR]): RXR - pharmacy/treatment route segment, required
        RXC (Optional[List[RXC]]): RXC - pharmacy/treatment component order segment, optional
        OBSERVATION (Optional[List[RDE_O01_OBSERVATION]]): optional
        CTI (Optional[List[CTI]]): CTI - clinical trial identification segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="ORC - common order segment",
    )

    ORDER_DETAIL: Optional[_RDE_O01_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
    )

    RXE: _RXE = Field(
        title="RXE",
        description="RXE - pharmacy/treatment encoded order segment",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="RXR - pharmacy/treatment route segment",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="RXC - pharmacy/treatment component order segment",
    )

    OBSERVATION: Optional[List[_RDE_O01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="CTI - clinical trial identification segment",
    )

    model_config = ConfigDict(populate_by_name=True)
