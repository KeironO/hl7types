"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RSP_K31.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CDO import CDO
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from ..segments.RXC import RXC
from ..segments.RXD import RXD
from ..segments.RXR import RXR
from .RSP_K31_ENCODING import RSP_K31_ENCODING
from .RSP_K31_OBSERVATION import RSP_K31_OBSERVATION
from .RSP_K31_ORDER_DETAIL import RSP_K31_ORDER_DETAIL
from .RSP_K31_TIMING import RSP_K31_TIMING

_CDO = CDO
_ORC = ORC
_PRT = PRT
_RSP_K31_ENCODING = RSP_K31_ENCODING
_RSP_K31_OBSERVATION = RSP_K31_OBSERVATION
_RSP_K31_ORDER_DETAIL = RSP_K31_ORDER_DETAIL
_RSP_K31_TIMING = RSP_K31_TIMING
_RXC = RXC
_RXD = RXD
_RXR = RXR


class RSP_K31_ORDER(BaseModel):
    """HL7 v2 RSP_K31.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[RSP_K31_TIMING]]): optional
        ORDER_DETAIL (Optional[RSP_K31_ORDER_DETAIL]): optional
        ENCODING (Optional[RSP_K31_ENCODING]): optional
        RXD (RXD): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        CDO (Optional[List[CDO]]): optional
        OBSERVATION (Optional[List[RSP_K31_OBSERVATION]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING: list[_RSP_K31_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ORDER_DETAIL: _RSP_K31_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    ENCODING: _RSP_K31_ENCODING | None = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    RXD: _RXD = Field(
        default=...,
        title="RXD",
        description="Required",
    )

    RXR: list[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: list[_RXC] | None = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    CDO: list[_CDO] | None = Field(
        default=None,
        title="CDO",
        description="Optional, repeating",
    )

    OBSERVATION: list[_RSP_K31_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
