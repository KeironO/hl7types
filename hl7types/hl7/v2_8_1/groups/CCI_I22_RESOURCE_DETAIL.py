"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCI_I22.RESOURCE_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .CCI_I22_RESOURCE_OBJECT import CCI_I22_RESOURCE_OBJECT
from .CCI_I22_RESOURCE_OBSERVATION import CCI_I22_RESOURCE_OBSERVATION

_CCI_I22_RESOURCE_OBJECT = CCI_I22_RESOURCE_OBJECT
_CCI_I22_RESOURCE_OBSERVATION = CCI_I22_RESOURCE_OBSERVATION


class CCI_I22_RESOURCE_DETAIL(BaseModel):
    """HL7 v2 CCI_I22.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CCI_I22_RESOURCE_OBJECT): required
        RESOURCE_OBSERVATION (Optional[List[CCI_I22_RESOURCE_OBSERVATION]]): optional
    """

    RESOURCE_OBJECT: _CCI_I22_RESOURCE_OBJECT = Field(
        default=...,
        title="RESOURCE_OBJECT",
        description="Required",
    )

    RESOURCE_OBSERVATION: list[_CCI_I22_RESOURCE_OBSERVATION] | None = Field(
        default=None,
        title="RESOURCE_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
