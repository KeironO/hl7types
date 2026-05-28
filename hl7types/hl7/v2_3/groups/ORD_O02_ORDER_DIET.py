"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORD_O02.ORDER_DIET
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.ODS import ODS
from ..segments.ORC import ORC

_NTE = NTE
_ODS = ODS
_ORC = ORC


class ORD_O02_ORDER_DIET(BaseModel):
    """HL7 v2 ORD_O02.ORDER_DIET group.

    Attributes:
        ORC (ORC): required
        ODS (Optional[List[ODS]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
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
