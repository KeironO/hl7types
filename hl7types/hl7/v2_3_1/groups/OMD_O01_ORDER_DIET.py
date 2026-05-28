"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OMD_O01.ORDER_DIET
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.ORC import ORC

from .OMD_O01_DIET import OMD_O01_DIET

_OMD_O01_DIET = OMD_O01_DIET
_ORC = ORC


class OMD_O01_ORDER_DIET(BaseModel):
    """HL7 v2 OMD_O01.ORDER_DIET group.

    Attributes:
        ORC (ORC): required
        DIET (Optional[OMD_O01_DIET]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    DIET: Optional[_OMD_O01_DIET] = Field(
        default=None,
        title="DIET",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
