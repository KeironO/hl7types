"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RDS_O13.ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXD import RXD
from ..segments.RXR import RXR

from .RDS_O13_ENCODING import RDS_O13_ENCODING
from .RDS_O13_OBSERVATION import RDS_O13_OBSERVATION
from .RDS_O13_ORDER_DETAIL import RDS_O13_ORDER_DETAIL
from .RDS_O13_TIMING import RDS_O13_TIMING

_FT1 = FT1
_NTE = NTE
_ORC = ORC
_RDS_O13_ENCODING = RDS_O13_ENCODING
_RDS_O13_OBSERVATION = RDS_O13_OBSERVATION
_RDS_O13_ORDER_DETAIL = RDS_O13_ORDER_DETAIL
_RDS_O13_TIMING = RDS_O13_TIMING
_RXC = RXC
_RXD = RXD
_RXR = RXR


class RDS_O13_ORDER(BaseModel):
    """HL7 v2 RDS_O13.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[RDS_O13_TIMING]]): optional
        ORDER_DETAIL (Optional[RDS_O13_ORDER_DETAIL]): optional
        ENCODING (Optional[RDS_O13_ENCODING]): optional
        RXD (RXD): required
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBSERVATION (Optional[List[RDS_O13_OBSERVATION]]): optional
        FT1 (Optional[List[FT1]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_RDS_O13_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ORDER_DETAIL: Optional[_RDS_O13_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ENCODING: Optional[_RDS_O13_ENCODING] = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    RXD: _RXD = Field(
        default=...,
        title="RXD",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
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

    OBSERVATION: Optional[List[_RDS_O13_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    FT1: Optional[List[_FT1]] = Field(
        default=None,
        title="FT1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
