"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RAS_O17.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTI import CTI
from ..segments.ORC import ORC
from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .RAS_O17_ENCODING import RAS_O17_ENCODING
from .RAS_O17_OBSERVATION import RAS_O17_OBSERVATION
from .RAS_O17_ORDER_DETAIL import RAS_O17_ORDER_DETAIL

_CTI = CTI
_ORC = ORC
_RAS_O17_ENCODING = RAS_O17_ENCODING
_RAS_O17_OBSERVATION = RAS_O17_OBSERVATION
_RAS_O17_ORDER_DETAIL = RAS_O17_ORDER_DETAIL
_RXA = RXA
_RXR = RXR


class RAS_O17_ORDER(BaseModel):
    """HL7 v2 RAS_O17.ORDER group.

    Attributes:
        ORC (ORC): required
        ORDER_DETAIL (Optional[RAS_O17_ORDER_DETAIL]): optional
        ENCODING (Optional[RAS_O17_ENCODING]): optional
        RXA (List[RXA]): required
        RXR (RXR): required
        OBSERVATION (Optional[List[RAS_O17_OBSERVATION]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ORDER_DETAIL: Optional[_RAS_O17_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ENCODING: Optional[_RAS_O17_ENCODING] = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    RXA: List[_RXA] = Field(
        default=...,
        title="RXA",
        description="Required, repeating",
    )

    RXR: _RXR = Field(
        default=...,
        title="RXR",
        description="Required",
    )

    OBSERVATION: Optional[List[_RAS_O17_OBSERVATION]] = Field(
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
