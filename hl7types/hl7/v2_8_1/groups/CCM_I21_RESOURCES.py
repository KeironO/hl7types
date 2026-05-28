"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCM_I21.RESOURCES
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RGS import RGS
from .CCM_I21_RESOURCE_DETAIL import CCM_I21_RESOURCE_DETAIL

_CCM_I21_RESOURCE_DETAIL = CCM_I21_RESOURCE_DETAIL
_RGS = RGS


class CCM_I21_RESOURCES(BaseModel):
    """HL7 v2 CCM_I21.RESOURCES group.

    Attributes:
        RGS (RGS): required
        RESOURCE_DETAIL (Optional[List[CCM_I21_RESOURCE_DETAIL]]): optional
    """

    RGS: _RGS = Field(
        default=...,
        title="RGS",
        description="Required",
    )

    RESOURCE_DETAIL: list[_CCM_I21_RESOURCE_DETAIL] | None = Field(
        default=None,
        title="RESOURCE_DETAIL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
