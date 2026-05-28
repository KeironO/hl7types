"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ORM_O01.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from .ORM_O01_CHOICE import ORM_O01_CHOICE

_NTE = NTE
_OBX = OBX
_ORM_O01_CHOICE = ORM_O01_CHOICE


class ORM_O01_ORDER_DETAIL(BaseModel):
    """HL7 v2 ORM_O01.ORDER_DETAIL group.

    Attributes:
        CHOICE (ORM_O01_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        OBX (Optional[List[OBX]]): optional
    """

    CHOICE: _ORM_O01_CHOICE = Field(
        default=...,
        title="CHOICE",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
