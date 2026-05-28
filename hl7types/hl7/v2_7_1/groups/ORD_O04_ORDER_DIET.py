"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ORD_O04.ORDER_DIET
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.ODS import ODS
from ..segments.ORC import ORC
from .ORD_O04_TIMING_DIET import ORD_O04_TIMING_DIET

_NTE = NTE
_ODS = ODS
_ORC = ORC
_ORD_O04_TIMING_DIET = ORD_O04_TIMING_DIET


class ORD_O04_ORDER_DIET(BaseModel):
    """HL7 v2 ORD_O04.ORDER_DIET group.

    Attributes:
        ORC (ORC): required
        TIMING_DIET (Optional[List[ORD_O04_TIMING_DIET]]): optional
        ODS (Optional[List[ODS]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING_DIET: list[_ORD_O04_TIMING_DIET] | None = Field(
        default=None,
        title="TIMING_DIET",
        description="Optional, repeating",
    )

    ODS: list[_ODS] | None = Field(
        default=None,
        title="ODS",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
