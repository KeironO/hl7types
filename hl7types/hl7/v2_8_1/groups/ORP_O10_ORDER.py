"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORP_O10.ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.PRT import PRT
from .ORP_O10_ORDER_DETAIL import ORP_O10_ORDER_DETAIL
from .ORP_O10_TIMING import ORP_O10_TIMING

_ORC = ORC
_ORP_O10_ORDER_DETAIL = ORP_O10_ORDER_DETAIL
_ORP_O10_TIMING = ORP_O10_TIMING
_PRT = PRT


class ORP_O10_ORDER(BaseModel):
    """HL7 v2 ORP_O10.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TIMING (Optional[List[ORP_O10_TIMING]]): optional
        ORDER_DETAIL (Optional[ORP_O10_ORDER_DETAIL]): optional
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

    TIMING: list[_ORP_O10_TIMING] | None = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ORDER_DETAIL: _ORP_O10_ORDER_DETAIL | None = Field(
        default=None,
        title="ORDER_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
