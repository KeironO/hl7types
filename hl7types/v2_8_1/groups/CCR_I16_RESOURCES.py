"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCR_I16.RESOURCES
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RGS import RGS

from .CCR_I16_RESOURCE_DETAIL import CCR_I16_RESOURCE_DETAIL

_CCR_I16_RESOURCE_DETAIL = CCR_I16_RESOURCE_DETAIL
_RGS = RGS


class CCR_I16_RESOURCES(BaseModel):
    """HL7 v2 CCR_I16.RESOURCES group.

    Attributes:
        RGS (RGS): required
        RESOURCE_DETAIL (Optional[List[CCR_I16_RESOURCE_DETAIL]]): optional
    """

    RGS: _RGS = Field(
        default=...,
        title="RGS",
        description="Required",
    )

    RESOURCE_DETAIL: Optional[List[_CCR_I16_RESOURCE_DETAIL]] = Field(
        default=None,
        title="RESOURCE_DETAIL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
