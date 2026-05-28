"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CQU_I19.RESOURCE_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .CQU_I19_RESOURCE_OBJECT import CQU_I19_RESOURCE_OBJECT
from .CQU_I19_RESOURCE_OBSERVATION import CQU_I19_RESOURCE_OBSERVATION

_CQU_I19_RESOURCE_OBJECT = CQU_I19_RESOURCE_OBJECT
_CQU_I19_RESOURCE_OBSERVATION = CQU_I19_RESOURCE_OBSERVATION


class CQU_I19_RESOURCE_DETAIL(BaseModel):
    """HL7 v2 CQU_I19.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CQU_I19_RESOURCE_OBJECT): required
        RESOURCE_OBSERVATION (Optional[List[CQU_I19_RESOURCE_OBSERVATION]]): optional
    """

    RESOURCE_OBJECT: _CQU_I19_RESOURCE_OBJECT = Field(
        default=...,
        title="RESOURCE_OBJECT",
        description="Required",
    )

    RESOURCE_OBSERVATION: list[_CQU_I19_RESOURCE_OBSERVATION] | None = Field(
        default=None,
        title="RESOURCE_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
