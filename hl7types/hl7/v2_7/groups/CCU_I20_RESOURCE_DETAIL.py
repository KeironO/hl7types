"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCU_I20.RESOURCE_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from .CCU_I20_RESOURCE_OBJECT import CCU_I20_RESOURCE_OBJECT

_CCU_I20_RESOURCE_OBJECT = CCU_I20_RESOURCE_OBJECT
_OBX = OBX


class CCU_I20_RESOURCE_DETAIL(BaseModel):
    """HL7 v2 CCU_I20.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CCU_I20_RESOURCE_OBJECT): required
        OBX (Optional[List[OBX]]): optional
    """

    RESOURCE_OBJECT: _CCU_I20_RESOURCE_OBJECT = Field(
        default=...,
        title="RESOURCE_OBJECT",
        description="Required",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
