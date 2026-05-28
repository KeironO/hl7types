"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCI_I22.RESOURCE_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBX import OBX

from .CCI_I22_RESOURCE_OBJECT import CCI_I22_RESOURCE_OBJECT

_CCI_I22_RESOURCE_OBJECT = CCI_I22_RESOURCE_OBJECT
_OBX = OBX


class CCI_I22_RESOURCE_DETAIL(BaseModel):
    """HL7 v2 CCI_I22.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CCI_I22_RESOURCE_OBJECT): required
        OBX (Optional[List[OBX]]): optional
    """

    RESOURCE_OBJECT: _CCI_I22_RESOURCE_OBJECT = Field(
        default=...,
        title="RESOURCE_OBJECT",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
