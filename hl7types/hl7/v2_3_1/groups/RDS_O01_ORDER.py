"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDS_O01.ORDER
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

from .RDS_O01_ENCODING import RDS_O01_ENCODING
from .RDS_O01_OBSERVATION import RDS_O01_OBSERVATION
from .RDS_O01_ORDER_DETAIL import RDS_O01_ORDER_DETAIL

_ORC = ORC
_RDS_O01_ENCODING = RDS_O01_ENCODING
_RDS_O01_OBSERVATION = RDS_O01_OBSERVATION
_RDS_O01_ORDER_DETAIL = RDS_O01_ORDER_DETAIL
_RXC = RXC
_RXD = RXD
_RXR = RXR


class RDS_O01_ORDER(HL7Model):
    """HL7 v2 RDS_O01.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[RDS_O01_ORDER_DETAIL]): optional
        ENCODING (Optional[RDS_O01_ENCODING]): optional
        RXD (RXD): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBSERVATION (Optional[List[RDS_O01_OBSERVATION]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_RDS_O01_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ENCODING: Optional[_RDS_O01_ENCODING] = Field(
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

    OBSERVATION: Optional[List[_RDS_O01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
