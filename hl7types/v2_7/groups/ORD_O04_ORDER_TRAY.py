"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORD_O04.ORDER_TRAY
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.ODT import ODT
from ..segments.ORC import ORC

from .ORD_O04_TIMING_TRAY import ORD_O04_TIMING_TRAY

_NTE = NTE
_ODT = ODT
_ORC = ORC
_ORD_O04_TIMING_TRAY = ORD_O04_TIMING_TRAY


class ORD_O04_ORDER_TRAY(BaseModel):
    """HL7 v2 ORD_O04.ORDER_TRAY group.

    Attributes:
        ORC (ORC): required
        TIMING_TRAY (Optional[List[ORD_O04_TIMING_TRAY]]): optional
        ODT (Optional[List[ODT]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING_TRAY: Optional[List[_ORD_O04_TIMING_TRAY]] = Field(
        default=None,
        title="TIMING_TRAY",
        description="Optional, repeating",
    )

    ODT: Optional[List[_ODT]] = Field(
        default=None,
        title="ODT",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
