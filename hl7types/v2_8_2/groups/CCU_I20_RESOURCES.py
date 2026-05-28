"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCU_I20.RESOURCES
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RGS import RGS

from .CCU_I20_RESOURCE_DETAIL import CCU_I20_RESOURCE_DETAIL

_CCU_I20_RESOURCE_DETAIL = CCU_I20_RESOURCE_DETAIL
_RGS = RGS


class CCU_I20_RESOURCES(BaseModel):
    """HL7 v2 CCU_I20.RESOURCES group.

    Attributes:
        RGS (RGS): required
        RESOURCE_DETAIL (Optional[List[CCU_I20_RESOURCE_DETAIL]]): optional
    """

    RGS: _RGS = Field(
        default=...,
        title="RGS",
        description="Required",
    )

    RESOURCE_DETAIL: Optional[List[_CCU_I20_RESOURCE_DETAIL]] = Field(
        default=None,
        title="RESOURCE_DETAIL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
