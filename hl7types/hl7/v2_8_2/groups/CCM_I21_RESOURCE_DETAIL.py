"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCM_I21.RESOURCE_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .CCM_I21_RESOURCE_OBJECT import CCM_I21_RESOURCE_OBJECT
from .CCM_I21_RESOURCE_OBSERVATION import CCM_I21_RESOURCE_OBSERVATION

_CCM_I21_RESOURCE_OBJECT = CCM_I21_RESOURCE_OBJECT
_CCM_I21_RESOURCE_OBSERVATION = CCM_I21_RESOURCE_OBSERVATION


class CCM_I21_RESOURCE_DETAIL(BaseModel):
    """HL7 v2 CCM_I21.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CCM_I21_RESOURCE_OBJECT): required
        RESOURCE_OBSERVATION (Optional[List[CCM_I21_RESOURCE_OBSERVATION]]): optional
    """

    RESOURCE_OBJECT: _CCM_I21_RESOURCE_OBJECT = Field(
        default=...,
        title="RESOURCE_OBJECT",
        description="Required",
    )

    RESOURCE_OBSERVATION: list[_CCM_I21_RESOURCE_OBSERVATION] | None = Field(
        default=None,
        title="RESOURCE_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
