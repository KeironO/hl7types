"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OMD_O03.ORDER_TRAY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.ODT import ODT
from ..segments.ORC import ORC

_NTE = NTE
_ODT = ODT
_ORC = ORC


class OMD_O03_ORDER_TRAY(BaseModel):
    """HL7 v2 OMD_O03.ORDER_TRAY group.

    Attributes:
        ORC (ORC): required
        ODT (List[ODT]): required
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
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
