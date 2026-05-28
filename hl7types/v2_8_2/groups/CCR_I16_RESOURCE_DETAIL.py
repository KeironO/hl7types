"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCR_I16.RESOURCE_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .CCR_I16_RESOURCE_OBJECT import CCR_I16_RESOURCE_OBJECT
from .CCR_I16_RESOURCE_OBSERVATION import CCR_I16_RESOURCE_OBSERVATION

_CCR_I16_RESOURCE_OBJECT = CCR_I16_RESOURCE_OBJECT
_CCR_I16_RESOURCE_OBSERVATION = CCR_I16_RESOURCE_OBSERVATION


class CCR_I16_RESOURCE_DETAIL(BaseModel):
    """HL7 v2 CCR_I16.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CCR_I16_RESOURCE_OBJECT): required
        RESOURCE_OBSERVATION (Optional[List[CCR_I16_RESOURCE_OBSERVATION]]): optional
    """

    RESOURCE_OBJECT: _CCR_I16_RESOURCE_OBJECT = Field(
        default=...,
        title="RESOURCE_OBJECT",
        description="Required",
    )

    RESOURCE_OBSERVATION: Optional[List[_CCR_I16_RESOURCE_OBSERVATION]] = Field(
        default=None,
        title="RESOURCE_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
