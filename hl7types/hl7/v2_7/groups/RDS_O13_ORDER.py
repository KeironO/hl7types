"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RDS_O13.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.PRT import PRT
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
_PRT = PRT
_RDS_O13_ENCODING = RDS_O13_ENCODING
_RDS_O13_OBSERVATION = RDS_O13_OBSERVATION
_RDS_O13_ORDER_DETAIL = RDS_O13_ORDER_DETAIL
_RDS_O13_TIMING = RDS_O13_TIMING
_RXC = RXC
_RXD = RXD
_RXR = RXR


class RDS_O13_ORDER(HL7Model):
    """HL7 v2 RDS_O13.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[RDS_O13_TIMING]]): optional
        ORDER_DETAIL (Optional[RDS_O13_ORDER_DETAIL]): optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        ENCODING (Optional[RDS_O13_ENCODING]): optional
        RXD (RXD): Pharmacy/Treatment Dispense, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
        OBSERVATION (Optional[List[RDS_O13_OBSERVATION]]): optional
        FT1 (Optional[List[FT1]]): Financial Transaction, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_RDS_O13_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    ORDER_DETAIL: Optional[_RDS_O13_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    ENCODING: Optional[_RDS_O13_ENCODING] = Field(
        default=None,
        title="ENCODING",
    )

    RXD: _RXD = Field(
        title="RXD",
        description="Pharmacy/Treatment Dispense",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
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

    OBSERVATION: Optional[List[_RDS_O13_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    FT1: Optional[List[_FT1]] = Field(
        default=None,
        title="FT1",
        description="Financial Transaction",
    )

    model_config = ConfigDict(populate_by_name=True)
