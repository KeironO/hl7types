"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCU_I20.RESOURCE_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .CCU_I20_RESOURCE_OBJECT import CCU_I20_RESOURCE_OBJECT
from .CCU_I20_RESOURCE_OBSERVATION import CCU_I20_RESOURCE_OBSERVATION

_CCU_I20_RESOURCE_OBJECT = CCU_I20_RESOURCE_OBJECT
_CCU_I20_RESOURCE_OBSERVATION = CCU_I20_RESOURCE_OBSERVATION


class CCU_I20_RESOURCE_DETAIL(BaseModel):
    """HL7 v2 CCU_I20.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CCU_I20_RESOURCE_OBJECT): required
        RESOURCE_OBSERVATION (Optional[List[CCU_I20_RESOURCE_OBSERVATION]]): optional
    """

    RESOURCE_OBJECT: _CCU_I20_RESOURCE_OBJECT = Field(
        default=...,
        title="RESOURCE_OBJECT",
        description="Required",
    )

    RESOURCE_OBSERVATION: Optional[List[_CCU_I20_RESOURCE_OBSERVATION]] = Field(
        default=None,
        title="RESOURCE_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
