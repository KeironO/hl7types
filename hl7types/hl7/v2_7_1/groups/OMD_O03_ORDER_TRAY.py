"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OMD_O03.ORDER_TRAY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.ODT import ODT
from ..segments.ORC import ORC
from .OMD_O03_TIMING_TRAY import OMD_O03_TIMING_TRAY

_NTE = NTE
_ODT = ODT
_OMD_O03_TIMING_TRAY = OMD_O03_TIMING_TRAY
_ORC = ORC


class OMD_O03_ORDER_TRAY(BaseModel):
    """HL7 v2 OMD_O03.ORDER_TRAY group.

    Attributes:
        ORC (ORC): required
        TIMING_TRAY (Optional[List[OMD_O03_TIMING_TRAY]]): optional
        ODT (List[ODT]): required
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    TIMING_TRAY: list[_OMD_O03_TIMING_TRAY] | None = Field(
        default=None,
        title="TIMING_TRAY",
        description="Optional, repeating",
    )

    ODT: list[_ODT] = Field(
        default=...,
        title="ODT",
        description="Required, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
